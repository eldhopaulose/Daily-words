# FastAPI Dictionary App

This is a simple app that uses FastAPI to serve a random list of words and their meanings from a csv file. You can also search for a word or a sub-word and get its meaning or related words.

## Installation

To install the app, you need to have Python 3.6 or higher and pip installed on your system. Then, follow these steps:

- Clone this repository or download the zip file.
- Navigate to the project directory and create a virtual environment using `python -m venv env`.
- Activate the virtual environment using `source env/bin/activate` on Linux/Mac or `env\Scripts\activate` on Windows.
- Install the required dependencies using `pip install -r requirements.txt`.
- Run the app using `uvicorn main:app --reload`.

## Usage

To use the app, you can either open your browser and go to `http://localhost:8000` or use a tool like curl or Postman to make requests to the app.

- To get a random list of words and their meanings, make a GET request to `/`.
- To search for a word or a sub-word and get its meaning or related words, make a POST request to `/word` with the word as a JSON string in the request body. For example, `{"input_word": "apple"}`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
