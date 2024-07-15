import logging
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_vertexai import VertexAI
import vertexai
logging.basicConfig(level=logging.INFO)
try:
    vertexai.init(project="x-avenue-425405-v4", location="us-central1")  # Update with your credentials
    file_path = "C:\\Users\\soura\\OneDrive\\Desktop\\More Work\\Lost in the Starless Sky.pdf"
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    embeddings = VertexAIEmbeddings(model_name="textembedding-gecko@001")  # Specify the model_name
    db = FAISS.from_documents(docs, embeddings)
    llm = VertexAI(model_name="text-bison@001")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        result = qa_chain({"query": query})
        answer = result['result']
        print(f"Chatbot: {answer}")
except Exception as e:
    logging.error(f"An error occurred: {e}")
