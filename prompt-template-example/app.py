from flask import Flask, redirect, url_for, request, render_template, session
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import (
    OpenAITextCompletion,
    AzureTextCompletion,
)

import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    # Read the values from the form
   prompt = request.form['text']
    
   kernel = sk.Kernel()

   deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
   kernel.add_text_completion_service(
       "dv", AzureTextCompletion(deployment, endpoint, api_key)
   )

   summarize = kernel.create_semantic_function(
        "{{$input}}\n\nOne line TLDR with the fewest words.."
   )
    # Retrieve the translation
   completion = summarize(prompt)

    # print(
    # summarize(
    #     """
    # 1st Law of Thermodynamics - Energy cannot be created or destroyed.
    # 2nd Law of Thermodynamics - For a spontaneous process, the entropy of the universe increases.
    # 3rd Law of Thermodynamics - A perfect crystal at zero Kelvin has zero entropy."""
    #     )
    # )

    # Call render template, passing the translated text,
    # original text, and target language to the template
   return render_template(
       'results.html',
       prompt = prompt,
        completion=completion.result
    )
