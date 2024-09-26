from secret_key import api_key
import os
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

os.environ['OPENAI_API_KEY'] = api_key

llm = OpenAI(temperature=0.6)

def generate_restaurant_name_and_items(selected_cuisine):
  # Chain 1: Restaurant name
  prompt_template_name = PromptTemplate(
    input_variables  = ['cuisine'],
    template = 'I want to open a restuarant for {cuisine} food. Suggest a fancy name for this.'
  )

  chain = prompt_template_name | llm

  # Chain 2: Menu items
  prompt_template_items = PromptTemplate(
    input_variables  = ['restaurant_name'],
    template = 'Suggest some menu items for {restuarant_name}. Return it as a comman separated list.'
  )

  chain_items = prompt_template_items | llm

  sequence_chain_name_items = {'restuarant_name': chain} | RunnablePassthrough.assign(menu_items=chain_items)
  response = sequence_chain_name_items.invoke(selected_cuisine)


  return response

if __name__ == '__main__':
  print(generate_restaurant_name_and_items('Indian'))