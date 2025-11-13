import subprocess
import sys

print("Git Push Script")
print("-" * 40)

# Get commit message from user
commit_message = input("Enter commit message: ").strip()

if not commit_message:
    print("Error: Commit message cannot be empty!")
    sys.exit(1)

print("\nExecuting git commands...\n")

# Git add
print("→ git add .")
result = subprocess.run(["git", "add", "."], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Error: {result.stderr}")
    sys.exit(1)
print("✓ Files staged")

# Git commit
print(f"\n→ git commit -m \"{commit_message}\"")
result = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Error: {result.stderr}")
    sys.exit(1)
print("✓ Changes committed")

# Git push
print("\n→ git push origin main")
result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
if result.returncode != 0:
    print(f"Error: {result.stderr}")
    sys.exit(1)
print("✓ Pushed to origin/main")

print("\n✓ Done!")
