
# Exercise 1

Your objective is to complete the code in both chat_bot.py and chat_app.py to craft a chatbot application leveraging the GPT model via the OpenAI API. Integrate this feature into the chat application within the file chat_app.py on Streamlit. Utilize the OpenAI API, specifically implementing the GPT 3.5 - Turbo model. For guidance on implementing the GPT Model through the OpenAI API, refer to the L0_openai_api.ipynb file or the util.py file.
<br>
class ChatBotGPT in file chat_bot.py
<br>

```python
# (...)
class ChatBotGPT:
    """
    Generate a response by using LLMs.
    """

    def __init__(self):
        self.memory = []

    def generate_response(self, message: str):
        return "Sorry, I need to be programmed 👨🏻‍💻"
# (...)
```

chat_bot.py

<br>

```python
# (...)

def initialize() -> None:
    """
    Initialize the app
    """

    st.sidebar.title("Simple chat (v3)")

    if "chatbot" not in st.session_state:
        st.session_state.chatbot = ChatBotGPT()

# (...)
```
