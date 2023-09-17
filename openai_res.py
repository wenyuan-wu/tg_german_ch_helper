import openai
import os
from dotenv import load_dotenv


def get_response_openai(input_text):
    """
    Function to get response from OpenAI API.
    :param input_text: string, input of the user text
    :return: string, output of the content
    """
    # load_dotenv()
    openai.api_key = os.environ.get('OPENAI_API')
    sys_prompt = "Sie sind ein schweizerdeutscher Übersetzer, Rechtschreibprüfer und Korrekturleser. Der Benutzer " \
                 "schreibt in einer beliebigen Sprache und Sie erkennen die Sprache, übersetzen sie und antworten mit " \
                 "der korrigierten und verbesserten Version des Eingabetextes in Schweizerdeutsch. Verwenden Sie für " \
                 "Pronomen der zweiten Person immer die vertraute Form. Geben Sie außerdem 2 alternative Versionen " \
                 "der Übersetzung und Erklärungen an."
    model = "gpt-3.5-turbo-16k-0613"
    messages = [
        {"role": "system", "content": f"{sys_prompt}"},
        {"role": "user", "content": f"{input_text}"}
    ]
    completion = openai.ChatCompletion.create(
        model=model,
        messages=messages,
    )
    # print(completion)
    message = completion["choices"][0]["message"]["content"]
    return message


def get_response_openai_test(prompt):
    """
    Function to test the message handling
    :param prompt: input prompt
    :return: reversed string
    """
    return prompt[::-1]


def main():
    input_text = "What are you guys going to do this weekend?"
    reply = get_response_openai(input_text)
    print(reply)


if __name__ == '__main__':
    main()
