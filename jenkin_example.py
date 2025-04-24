import sys
import io

def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    print("🔧 Jenkins CI/CD Demo Running... (but now with GitHub Actions!)")
    print("This is a simple pipeline demo!")
    print("✅ All systems go!")

if _name_ == "_main_":
    main()
