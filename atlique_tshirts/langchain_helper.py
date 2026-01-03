from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_experimental.sql.prompt import MYSCALE_PROMPT,PROMPT_SUFFIX,VECTOR_SQL_PROMPT
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate

import os
from few_shots import few_shots
from dotenv import load_dotenv
load_dotenv()

def get_few_shot_db_chain():
  llm = ChatOpenAI(
      model="gpt-3.5-turbo",
      api_key=os.environ["api_key"],
      base_url="https://openrouter.ai/api/v1",
      temperature=0
  )

  db_user = "root"
  db_password = "root"
  db_host = "127.0.0.1"
  db_name = "atliq_tshirts"

  db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)  

  embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
  to_vectorize = [" ".join(example.values()) for example in few_shots ]
  vectorstore = Chroma.from_texts(to_vectorize , embedding=embeddings, metadatas=few_shots)
  example_selectors = SemanticSimilarityExampleSelector(
  vectorstore = vectorstore,
  k=2,
  )

  example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
    template="""
    Question: {Question}
    SQLQuery: {SQLQuery}
    SQLResult: {SQLResult}
    Answer: {Answer}
    """
    )

  few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selectors,     # ✅ singular
    example_prompt=example_prompt,
    prefix=MYSCALE_PROMPT.template,        # ✅ string, not object
    suffix=PROMPT_SUFFIX,
    input_variables=["input", "table_info", "top_k"]
    ) 
  
  chain = SQLDatabaseChain.from_llm(
    llm=llm,
    db=db,
    prompt=few_shot_prompt,
    verbose=True,
    
    )
  return chain

if __name__ == "__main__":
  chain = get_few_shot_db_chain()
  print(chain.invoke("How many total t shirts are left in total in stock?"))

