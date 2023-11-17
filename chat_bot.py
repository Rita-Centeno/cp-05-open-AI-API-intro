
"""
ChatBot classes
"""

import random

# [i]                                                                                            #
# [i] Static ChatBot                                                                             -
# [i]                                                                                            #

class ChatBotStatic:
    """
    ChatBot class
    """

    def __init__(self):
        self.memory = []

    def generate_response(self, message: str):
        """
        Returns a static response
        """
        return "How can I help you?"

    def __str__(self):
        shift = "   "
        class_name = str(type(self)).split('.')[-1].replace("'>", "")

        return f"🤖 {class_name}."

# [i]                                                                                            #
# [i] Static ChatBot                                                                             -
# [i]                                                                                            #

class ChatBotRandom:
    """
    ChatBotRandom class provides a simple chatbot that generates random responses.
    """

    def __init__(self):
        self.memory = []

    def generate_response(self, message: str):
        """
        Generates a random response for incoming messages.

        Returns:
            str: A randomly selected response from a list of greeting messages.

        """
        return random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )

"""
[!] For the upcoming class, kindly incorporate your chatbot with access to GPT3.5 Turbo via the OpenAI API.
"""

# [i]                                                                                            #
# [i] ChatBot GPT                                                                                #
# [i]                                                                                            #

class ChatBotGPT:
    """
    Generate a response by using LLMs.
    """

    def __init__(self, engine):
        self.memory = []

        self.engine = engine

    def generate_response(self, message: str):
        return self.engine.get_completion(prompt=message)


