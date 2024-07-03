import boto3 
import json
import base64
import os
# {
#  "modelId": "stability.stable-diffusion-xl-v1",
#  "contentType": "application/json",
#  "accept": "application/json",
#  "body": "{\"text_prompts\":[{\"text\":\"this is where you place your input text\",\"weight\":1}],\"cfg_scale\":10,\"seed\":0,\"steps\":50,\"width\":512,\"height\":512}"
# }

prompt_data="""
Create a image of twin towers in dessert
"""
prompt_template=[{"text":prompt_data,"weight":1}]
bedrock=boto3.client(service_name="bedrock-runtime")
payload={
    "text_prompts":prompt_template,
    "cfg_scale":10,
    "seed":0,
    "steps":50,
    "width":512,
    "height":512

    
}
body=json.dumps(payload)
model_id="stability.stable-diffusion-xl-v1"
response=bedrock.invoke_model(
    body=body,
    modelId=model_id,
    contentType="application/json",
    accept="application/json"
)
response_body = json.loads(response.get("body").read())
print(response_body)
artifact = response_body.get("artifacts")[0]
image_encoded = artifact.get("base64").encode("utf-8")
image_bytes = base64.b64decode(image_encoded)

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
file_name = f"{output_dir}/generated-img.png"
with open(file_name, "wb") as f:
    f.write(image_bytes)