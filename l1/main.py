from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
# updated ReAct
def main():
    print("Hello from l1!")
    print(os.environ.get("NVIDIA_API_KEY"))


if __name__ == "__main__":
    main()
