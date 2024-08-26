Microsoft Windows [版本 10.0.19045.4780]
(c) Microsoft Corporation。保留所有权利。

C:\Users\10508>python -m this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

C:\Users\10508>python get-pip.py
python: can't open file 'C:\\Users\\10508\\get-pip.py': [Errno 2] No such file or directory

C:\Users\10508>cd downloads

C:\Users\10508\Downloads>python get-pip.py
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Collecting pip
  Using cached pip-24.2-py3-none-any.whl.metadata (3.6 kB)
Using cached pip-24.2-py3-none-any.whl (1.8 MB)
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 24.2
    Uninstalling pip-24.2:
      Successfully uninstalled pip-24.2
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Successfully installed pip-24.2

C:\Users\10508\Downloads>pip3 install zhipuai
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Requirement already satisfied: zhipuai in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (2.1.4.20230814)
Requirement already satisfied: cachetools>=4.2.2 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from zhipuai) (5.5.0)
Requirement already satisfied: httpx>=0.23.0 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from zhipuai) (0.27.0)
Requirement already satisfied: pydantic<3.0,>=1.9.0 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from zhipuai) (2.8.2)
Requirement already satisfied: pydantic-core>=2.14.6 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from zhipuai) (2.20.1)
Requirement already satisfied: pyjwt<2.9.0,>=2.8.0 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from zhipuai) (2.8.0)
Requirement already satisfied: anyio in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from httpx>=0.23.0->zhipuai) (4.4.0)
Requirement already satisfied: certifi in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from httpx>=0.23.0->zhipuai) (2024.7.4)
Requirement already satisfied: httpcore==1.* in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from httpx>=0.23.0->zhipuai) (1.0.5)
Requirement already satisfied: idna in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from httpx>=0.23.0->zhipuai) (3.7)
Requirement already satisfied: sniffio in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from httpx>=0.23.0->zhipuai) (1.3.1)
Requirement already satisfied: h11<0.15,>=0.13 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from httpcore==1.*->httpx>=0.23.0->zhipuai) (0.14.0)
Requirement already satisfied: annotated-types>=0.4.0 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from pydantic<3.0,>=1.9.0->zhipuai) (0.7.0)
Requirement already satisfied: typing-extensions>=4.6.1 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from pydantic<3.0,>=1.9.0->zhipuai) (4.12.2)
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)

C:\Users\10508\Downloads>pip3 install uvicorn
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Collecting uvicorn
  Downloading uvicorn-0.30.6-py3-none-any.whl.metadata (6.6 kB)
Collecting click>=7.0 (from uvicorn)
  Downloading click-8.1.7-py3-none-any.whl.metadata (3.0 kB)
Requirement already satisfied: h11>=0.8 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from uvicorn) (0.14.0)
Collecting colorama (from click>=7.0->uvicorn)
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Downloading uvicorn-0.30.6-py3-none-any.whl (62 kB)
Downloading click-8.1.7-py3-none-any.whl (97 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Installing collected packages: colorama, click, uvicorn
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Successfully installed click-8.1.7 colorama-0.4.6 uvicorn-0.30.6

C:\Users\10508\Downloads>pip3 install fastapi
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Collecting fastapi
  Downloading fastapi-0.112.2-py3-none-any.whl.metadata (27 kB)
Collecting starlette<0.39.0,>=0.37.2 (from fastapi)
  Downloading starlette-0.38.2-py3-none-any.whl.metadata (5.9 kB)
Requirement already satisfied: pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from fastapi) (2.8.2)
Requirement already satisfied: typing-extensions>=4.8.0 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from fastapi) (4.12.2)
Requirement already satisfied: annotated-types>=0.4.0 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi) (0.7.0)
Requirement already satisfied: pydantic-core==2.20.1 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from pydantic!=1.8,!=1.8.1,!=2.0.0,!=2.0.1,!=2.1.0,<3.0.0,>=1.7.4->fastapi) (2.20.1)
Requirement already satisfied: anyio<5,>=3.4.0 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from starlette<0.39.0,>=0.37.2->fastapi) (4.4.0)
Requirement already satisfied: idna>=2.8 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from anyio<5,>=3.4.0->starlette<0.39.0,>=0.37.2->fastapi) (3.7)
Requirement already satisfied: sniffio>=1.1 in c:\users\10508\appdata\local\programs\python\python312\lib\site-packages (from anyio<5,>=3.4.0->starlette<0.39.0,>=0.37.2->fastapi) (1.3.1)
Downloading fastapi-0.112.2-py3-none-any.whl (93 kB)
Downloading starlette-0.38.2-py3-none-any.whl (72 kB)
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Installing collected packages: starlette, fastapi
WARNING: Ignoring invalid distribution ~ (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
WARNING: Ignoring invalid distribution ~ip (C:\Users\10508\AppData\Local\Programs\Python\Python312\Lib\site-packages)
Successfully installed fastapi-0.112.2 starlette-0.38.2

C:\Users\10508\Downloads>python demo.py
CompletionMessage(content='好的，让我们解决这个问题。这是一个典型的“鸡和牛”问题，通常可以通过设立方程来解决。\n\n设鸡 的数量为 x，牛的数量为 y。\n\n根据题目，我们有两个方程：\n\n1. 鸡和牛的总数量：x + y = 35\n2. 鸡和牛的脚的总数量：2x + 4y = 94\n\n现在我们来解这个方程组。\n\n首先，从第一个方程中，我们可以表达 y 为 x 的函数：\ny = 35 - x\n\n然后我们将这个表达式代入第二个方程中：\n2x + 4(35 - x) = 94\n2x + 140 - 4x = 94\n-2x = 94 - 140\n-2x = -46\nx = 23\n\n现在我们知道鸡的数量是 23，我们可以用第一个方程来找出牛的数量：\ny = 35 - x\ny = 35 - 23\ny = 12\n\n所以，鸡有 23 头，牛有 12 头。\n\n这是我的解法和推理过程。如果你已经尝试解决这个问题并得到了一个答案，你可以告诉我你的答案，我将比较并评估它。', role='assistant', tool_calls=None)

C:\Users\10508\Downloads>python main.py
[32mINFO[0m:     Will watch for changes in these directories: ['C:\\Users\\10508\\Downloads']
[32mINFO[0m:     Uvicorn running on [1mhttp://0.0.0.0:8800[0m (Press CTRL+C to quit)
[32mINFO[0m:     Started reloader process [[36m[1m17676[0m] using [36m[1mStatReload[0m
[32mINFO[0m:     Started server process [[36m13332[0m]
[32mINFO[0m:     Waiting for application startup.
[32mINFO[0m:     Application startup complete.
