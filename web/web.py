# 在页面输入问题，调用 ask_llm()，然后把回答显示出来
# 只要做五件事：
# 1. 导入 Streamlit
# 2. 导入 ask_llm()
# 3. 画页面
# 4. 接收用户输入
# 5. 点击按钮后调用模型并显示结果

import streamlit as st
from ai.agent import ask_llm   # 从 ai/agent.py 导入 ask_llm 函数

# 页面配置
st.set_page_config(page_title="AI for Test Analysis", page_icon="🤖", layout="wide")

# 页面标题
st.title("AI for Test Analysis")
st.write("Ask a question and get a response from the LLM.")

# 输入框：API Key 和问题
# type="password" 的意思是输入时隐藏内容
api_key = st.text_input("API Key (optional if set in .env)", type="password")
question = st.text_area("Enter your question:")

# 按钮
if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            # 显示加载提示
            with st.spinner("Thinking..."):
                answer = ask_llm(question=question, api_key=api_key or None)
            st.subheader("Answer")
            st.write(answer)
        except Exception as e:
            st.error(f"Failed to get response: {type(e).__name__}: {e}")