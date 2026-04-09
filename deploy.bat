:: 把执行过程打印出来
@echo on
:: py和python的区别：py更兼容，它能自己去找到你本机装的 Python
py -m streamlit run web/web.py

::使用方法：
::1. 双击运行
::2. 在命令行中运行：在项目根目录运行 .\deploy.bat