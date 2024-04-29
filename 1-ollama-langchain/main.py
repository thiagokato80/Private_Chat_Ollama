import langchain
from langchain_core.prompts import PromptTemplate

from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.llms import Ollama

llm = Ollama(
    model="mistral", 
    #callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
    verbose=False
)
#llm = Ollama(model="llama3")

question = "Me dê uma desculpa curta para não ir a uma festa"

#prompt_template = PromptTemplate.from_template(question)

chain = llm

print(chain.invoke(question))