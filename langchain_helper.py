from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secrete_key import openapi_key
import os
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.7)

def generate_company_name_and_services(company):
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate(
        input_variables=['company'],
        template="I want to get services from {company}. Suggest some services for customers."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="company_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate(
        input_variables=['company_name'],
        template="""Suggest some services for {company_name}. Return it as a comma separated string"""
    )

    service_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="service_items")

    chain = SequentialChain(
        chains=[name_chain, service_items_chain],
        input_variables=['company'],
        output_variables=['company_name', "service_items"]
    )

    response = chain({'company': company})

    return response

if __name__ == "__main__":
    print(generate_company_name_and_services("Google"))
