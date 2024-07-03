import boto3 
import json
# {
#  "modelId": "meta.llama3-8b-instruct-v1:0",
#  "contentType": "application/json",
#  "accept": "application/json",
#  "body": "{\"prompt\":\"this is where you place your input text\",\"max_gen_len\":512,\"temperature\":0.5,\"top_p\":0.9}"
# }

prompt_data="""
Write a poem on monster anime """
bedrock=boto3.client(service_name="bedrock-runtime")
payload={
    "prompt":prompt_data,
    "max_gen_len":512,
    "temperature":0.8,
    "top_p":0.9
}

body= json.dumps(payload)
response=bedrock.invoke_model(
    body=body,
    modelId="meta.llama3-8b-instruct-v1:0",
    contentType="application/json",
    accept="application/json"
    
)
response_body=json.loads(response.get("body").read())
response_text=response_body['generation']
print(response_text)