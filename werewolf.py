# coding=utf-8
import openai
import json
import os
import requests

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

# 配置OpenAI API凭证
openai.api_key = " "
message="介绍一下你自己"

def chatgpt(message):
    # 发送请求
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s"% openai.api_key
    }
    data = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [{"role": "user", "content": "%s" % message}],
        "temperature": 0.7
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return response.json().get("choices")[0].get("message").get("content")

# print(chatgpt("你好吗"))



num = input("几人游戏?")
num = int(num)
if (num%2 == 0):
    num = num+1

group = []
group.append("seer")
group.append("hunter")
group.append("witch")
for i in range(int((num-3)/2)):
    group.append("wolf")
    group.append("human")
print(group)

# night time

