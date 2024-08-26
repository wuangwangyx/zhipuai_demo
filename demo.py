from zhipuai import ZhipuAI
client = ZhipuAI(api_key="98f72a7c339be34e99266e85437de25d.QMk7YAe3mQRTIRAa")  # ****这里填写我们的APIKey即可
response = client.chat.completions.create(
    model="glm-4",  # 填写需要调用的模型名称
    messages=[
        {"role": "system", "content":"作为一个AI助手，你的任务是帮助用户解决复杂的数学问题。对于每个问题，你需要首先独立解决它，然后比较和评估用户的答案，并最终提供反馈。在这个过程中，请展示你的每一步推理过程。我有一个数学问题需要帮助:"},
        {"role": "user", "content": "问题是：一个农场有鸡和牛共 35 头，脚总共有 94 只。鸡和牛各有多少头？"}
    ]
)
print(response.choices[0].message)