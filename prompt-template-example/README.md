# OpenAI at Scale - Prompt Template Demo
# OpenAI API Quickstart - Python example app

Example web app leveraging Azure OpenAI with a [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd prompt-template-example
   ```

4. Create a new virtual environment:

   ```bash
   $ python3 -m venv flask-web-env 
   $ source flask-web-env/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! For the full context behind this example app, check out the [tutorial](https://beta.openai.com/docs/quickstart).
