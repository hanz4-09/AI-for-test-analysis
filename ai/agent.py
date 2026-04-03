import os
import httpx
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# get_llm()：创建并返回一个可以调用大模型的对象
# 参数：
#   api_key: 可选，如果提供了API密钥，则使用该密钥 - 比如 Streamlit 页面上让用户输入
#           否则从环境变量中获取
#  -> ChatOpenAI：返回值类型标注 - 这个函数预计返回一个 ChatOpenAI 对象
def get_llm(api_key: str | None = None) -> ChatOpenAI:
    # 从环境变量里读取GENAI_BASE_URL，如果没读到，就用默认值：https://api.kimi.com/coding/v1
    base_url = os.getenv("GENAI_BASE_URL", "https://api.kimi.com/coding/v1")
    # 读模型名
    model = os.getenv("GENAI_MODEL", "kimi-for-coding")
    # 读API key
    resolved_api_key = api_key or os.getenv("GENAI_API_KEY")

    return ChatOpenAI(
        model=model,
        api_key=resolved_api_key,
        base_url=base_url,
        http_client=httpx.Client(),
    )

# ask_llm(): 接收一个问题 question，返回一个字符串回答
def ask_llm(question: str, api_key: str | None = None) -> str:
    # question 是不是空值
    # strip() 去除首尾空格，如果输入是"    "，strip() 之后还是空值
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    llm = get_llm(api_key=api_key)
    response = llm.invoke(question.strip())
    return response.content