import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")
embedding_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")

missing_settings = [
    name
    for name, value in (
        ("AZURE_OPENAI_ENDPOINT", endpoint),
        ("AZURE_OPENAI_DEPLOYMENT", deployment_name),
        ("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", embedding_deployment),
        ("AZURE_OPENAI_API_KEY", api_key),
    )
    if not value
]
if missing_settings:
    raise ValueError(
        f"Missing required settings: {', '.join(missing_settings)}. "
        "Set them in .env or the environment."
    )

client = OpenAI(
    base_url=endpoint,
    api_key=api_key,
)

response = client.responses.create(
    model=deployment_name,
    input="plan trip 3 ngày đi Trung Quốc bao gồm Thượng Hải, Hàng Châu, Tô Châu",
    reasoning={"effort": "medium"},
)
print(f"answer: {response.output_text}")

embedding_response = client.embeddings.create(
    model=embedding_deployment,
    input="Thượng Hải, Hàng Châu, Tô Châu",
)
print(f"Embedding dimensions: {len(embedding_response.data[0].embedding)}")
embedding = embedding_response.data[0].embedding
print(f"Embedding preview (first 10 values): {embedding[:10]}")
