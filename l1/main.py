from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print("Hello from l1!")
    print(os.environ.get("NVIDIA_API_KEY"))


if __name__ == "__main__":
    main()
