import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import sys

def test_openai():
    print("🔥 Testing Azure OpenAI vars... Let's go! 😎")
    load_dotenv()
    
    # Grab env vars
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")
    chat_deployment = os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    embedding_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
    
    # Check if vars exist
    if not all([endpoint, api_key, api_version, chat_deployment, embedding_deployment]):
        print("🚨 Missing some OpenAI env vars! Check your .env file.")
        sys.exit(1)
    
    try:
        # Set up Azure OpenAI client
        client = AzureOpenAI(
            azure_endpoint=endpoint,
            api_key=api_key,
            api_version=api_version
        )
        
        # Test chat completion
        print("🗣️ Testing chat deployment...")
        chat_response = client.chat.completions.create(
            model=chat_deployment,
            messages=[{"role": "user", "content": "Yo, just testing! Say hi!"}],
            max_tokens=10
        )
        print(f"✅ Chat test passed! Response: {chat_response.choices[0].message.content}")
        
        # Test embedding
        print("📊 Testing embedding deployment...")
        embedding_response = client.embeddings.create(
            model=embedding_deployment,
            input="Test this out!"
        )
        print(f"✅ Embedding test passed! Got {len(embedding_response.data[0].embedding)} dims.")
        
        print("🎉 All OpenAI vars are vibin'!")
        
    except Exception as e:
        print(f"💥 Oops, something broke! Error: {str(e)}")
        print("👀 Double-check AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_KEY, AZURE_OPENAI_API_VERSION, "
              "AZURE_OPENAI_CHAT_DEPLOYMENT_NAME, or AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME.")
        sys.exit(1)

if __name__ == "__main__":
    test_openai()
