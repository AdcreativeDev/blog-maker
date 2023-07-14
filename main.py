import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
import os
from PIL import Image

st.set_page_config(
    page_title="🦜🔗 Blog Outline Generator",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
image = Image.open("blog-banner.jpg")
st.image(image, caption='created by MJ')

st.title("🗒 :blue[Blog Generator]")

system_openai_api_key = os.environ.get('OPENAI_API_KEY')
system_openai_api_key = st.text_input(":key: **Step 1 - OpenAI Key** :", value=system_openai_api_key)
os.environ["OPENAI_API_KEY"] = system_openai_api_key


template = """
    Objective : Write a creative online Sales and Promotion blog content based on {topic}

    Your role : Act as a  business consultant and marketing content provider.

    Your task : Write a sales promotion blog to customers, the content is to explain why your company should use our professional AI chatbot services using the latest technologies : Openai, telegram, Langchain , text to speech and whatsapp api.

    Promote our customer service chatbot with AI smart functions to answer customer enquiry , product search to enhance the shopping experience.

    
    Finally, List out 5 major advantages of our chatbot  solution in point form.
"""

def generate_response(topic):
  llm = OpenAI(model_name='text-davinci-003', openai_api_key=system_openai_api_key)
  # Prompt

  

  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)

with st.form('myform'):
  with st.expander("Prompt Template"):
      st.code(template)

  topic_text = st.text_input('**Step 2 - Enter Service name to generate the blog** :', '')
  submitted = st.form_submit_button('Submit')
  if not system_openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and system_openai_api_key.startswith('sk-'):
    with st.spinner('Generating ...'):
      generate_response(topic_text)

