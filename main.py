from typing import Optional

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from zhipuai import ZhipuAI


client = ZhipuAI(api_key="47bbc6c67f380547166fa01d5b488edc.IgZmzrqaOTitNV4n")  # ****这里填写我们的APIKey即可

app = FastAPI()


class QueryParams(BaseModel):
    query: str
    instruction: Optional[str] = None


def query_model_data(query_str: str, instruction: Optional[str]):
    messages = []
    if instruction:
        messages.append({"role": "system", "content": instruction})

    messages.append({"role": "user", "content": query_str})
    response = client.chat.completions.create(
        model="glm-4",  # 填写需要调用的模型名称
        messages = messages
    )
    return response.choices[0].message


@app.get('/index', response_class=HTMLResponse)
async def index():
    return """
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <h1> 我的机器人助理 </h1>
            <p>背景:<textarea id="instruction" name="instruction" rows="5" cols="60"></textarea><p>
            <p>问题:<textarea id="query" name="query" rows="3" cols="60"></textarea><p>
            <p>回答:<textarea id="answer" name="answer" rows="8" cols="60"></textarea><p>
            <button type="button" onclick="updateTable()">提问</button>
        <script>
        function updateTable() {
            var query = document.getElementById('query').value;
            var instruction = document.getElementById('instruction').value;
            var answer = document.getElementById("answer");
            sendQuery(query, instruction)
            answer.innerHTML = "正在回答中....... 请稍等";
        }


        function sendQuery(query, instruction) {
            var answer = document.getElementById("answer");
            var xhr = new XMLHttpRequest();
            var url = "/chat";
            var dataToSend = JSON.stringify({"query": query, "instruction": instruction});

            const controller = new AbortController()
            const timeoutId = setTimeout(() => controller.abort(), 10000)

            fetch(url, {
                credentials: "same-origin",
                mode: "same-origin",
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: dataToSend
            })
            .then((response) => response.json())
            .then((json) => {answer.innerHTML = json['content']});

        }
        </script>
        </body>
    </html>
    """
            # <form action="/chat", method="post">
            #     背景: <input type="text" name="instruction"><br>
            #     问题: <input type="text" name="query"><br>
            #     <input type="submit" value="提交">
            # </form>


@app.post('/chat')
async def chat(query: QueryParams):
    print(query.query)
    print(query.instruction)
    data = query_model_data(query.query, query.instruction)
    print(data)
    return data


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8800,reload=True)