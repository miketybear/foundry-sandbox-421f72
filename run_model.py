from openai import OpenAI

endpoint = "https://bd-foundry-bpm.services.ai.azure.com/openai/v1"
deployment_name = "gpt-6-luna"
api_key = "<api-key>"

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

response = client.responses.create(
    model=deployment_name,
    input="plan trip 3 ngày đi Trung Quốc bao gồm Thượng Hải, Hàng Châu, Tô Châu",
    reasoning={"effort": "medium"},
)

print(f"answer: {response.output_text}")
