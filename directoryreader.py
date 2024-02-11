from llama_index.llms import Gemini
from llama_index.readers import SimpleDirectoryReader
from llama_index import VectorStoreIndex
import llama_index
import os
from dotenv import load_dotenv

load_dotenv()

def main(url:str)->None:
    document=SimpleDirectoryReader(html_to_text=True).load_data(urls=[url])
    index=VectorStoreIndex.from_document(documents=document)
    query_engine=index.as_query_engine()
    response=query_engine.query("What are the main features mentioned in this blog")
    print(response)


if __name__ == "__main__":
    main(url="https://blog.llamaindex.ai/llamaindex-gemini-8d7c3b9ea97e")
