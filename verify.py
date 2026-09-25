import sys
import hashlib
from pathlib import Path

def verify_evidence(artifact_dir: str):
    print("--- Starting Independent Verification ---")
    evidence_file = Path(artifact_dir) / "test-evidence.txt"
    checksum_file = Path(artifact_dir) / "test-evidence.sha256"
    
    if not evidence_file.exists() or not checksum_file.exists():
        print("❌ ERROR: Evidence files are missing!")
        sys.exit(1)
        
    # 1. Read the actual evidence file as bytes
    evidence_bytes = evidence_file.read_bytes()
    
    # 2. Calculate SHA-256 independently
    calculated_hash = hashlib.sha256(evidence_bytes).hexdigest()
    print(f"Calculated Hash: {calculated_hash}")
    
    # 3. Read the recorded checksum
    recorded_hash = checksum_file.read_text().strip()
    print(f"Recorded Hash:   {recorded_hash}")
    
    # 4. Compare them
    if calculated_hash == recorded_hash:
        print("Verification PASSED ✅")
    else:
        print("Verification FAILED ❌: Checksums do not match!")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify.py <artifact_dir>")
        sys.exit(1)
    verify_evidence(sys.argv[1])