import os
from dotenv import load_dotenv
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import sys

def test_search():
    print("🔍 Testing Azure AI Search vars... Let's do this! 😎")
    load_dotenv()
    
    # Grab env vars
    endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
    api_key = os.getenv("AZURE_SEARCH_API_KEY")
    
    # Check if vars exist
    if not all([endpoint, api_key]):
        print("🚨 Missing some Search env vars! Check your .env file.")
        sys.exit(1)
    
    try:
        # Set up Search client (using a dummy index name to test connection)
        credential = AzureKeyCredential(api_key)
        client = SearchClient(endpoint=endpoint, index_name="test-index", credential=credential)
        
        # Test listing indexes to verify connection
        print("📋 Testing search service connection...")
        # Instead of listing indexes directly, we'll just try to initialize the client properly
        # If the endpoint or key is wrong, this will fail
        client.get_document_count()  # Simple call to test connectivity (index may not exist, but will test auth)
        print("✅ Search service connection test passed! Endpoint and key are good.")
        
        print("🎉 All Search vars are lit!")
        
    except Exception as e:
        print(f"💥 Uh-oh, something went wrong! Error: {str(e)}")
        print("👀 Double-check AZURE_SEARCH_SERVICE_ENDPOINT or AZURE_SEARCH_API_KEY.")
        print("Note: If the error mentions the index, the connection is likely fine, but 'test-index' doesn't exist.")
        sys.exit(1)

if __name__ == "__main__":
    test_search()
