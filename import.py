import weaviate
import json

client = weaviate.Client(
    url = "https://test1-9rci97dc.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="YOUR-KEY"),  # Replace w/ your Weaviate instance API key
    additional_headers = {
        "X-HuggingFace-Api-Key": "YOUR-KEY",  # Replace with your inference API key
        "X-OpenAI-Api-Key": "YOUR-KEY",  # Replace with your API key
    }
)
""" we already created the schema in the database
# ===== add schema =====
class_obj = {
    "class": "Question2",
    "vectorizer": "text2vec-huggingface",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    "moduleConfig": {"generative-openai": {},
        "text2vec-huggingface": {
            "model": "sentence-transformers/all-MiniLM-L6-v2",  # Can be any public or private Hugging Face model.
            "options": {
                "waitForModel": True
            }
        }
    }
}

"""

""" we have already previously imported the data
client.schema.create_class(class_obj)

# ===== import data =====
# Load data
import requests
url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny.json'
resp = requests.get(url)
data = json.loads(resp.text)

# Configure a batch process
with client.batch(
    batch_size=100
) as batch:
    # Batch import all Questions
    for i, d in enumerate(data):
        print("importing question: {i+1}")

        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }

        client.batch.add_data_object(
            properties,
            "Question2",
        )
"""

#client = weaviate.Client("https://test1-9rci97dc.weaviate.network")  # Replace with your endpoint
some_objects = client.data_object.get()
print(json.dumps(some_objects))

# instruction for the generative module
generatePrompt = "Write an answer to the question that is similar to answer: {question}{answer}"

result = (
  client.query
  .get("Question2", ["question", "answer"])
  .with_generate(single_prompt=generatePrompt)
  .with_near_text({
    "concepts": ["glycogen"]
  })
  .with_limit(5)
).do()

print(result)

"""
What Accomplished:
1. able to install Wevaite and Hugging Face's sample database


Where Stuck:
1. Unable to connect to OpenAI despite paying for it
"""