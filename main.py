import random
import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Load csv file
nba = pd.read_csv("DIct.csv")

@app.get("/")
async def root():
    # Generate 5 random numbers between 0 and len(nba)
    random_numbers = random.sample(range(0, len(nba)), 5)
    # Create a list of dictionaries containing the randomly selected rows
    word_list = []
    for i in random_numbers:
        row_dict = nba.loc[[i]].to_dict(orient='records')[0]
        word_list.append(row_dict)
    return {"words": word_list}

@app.post("/word")
async def get_word_meaning(input_word: str):
    # Load dictionary DataFrame
    columns = ['english_word', 'malayalam_definition']
    df = pd.read_csv("DIct.csv", header=None, names=columns, skiprows=1)

    # Convert input word to lowercase
    input_word = input_word.strip().lower()

    # Find all rows that contain the input word or sub-word
    result = df.loc[df['english_word'].str.lower().str.contains(input_word)]

    # If rows are found, return the meanings
    if not result.empty:
        # Filter rows that contain the exact input word
        exact_matches = result[result['english_word'].str.lower() == input_word]
        if not exact_matches.empty:
            meanings = exact_matches['malayalam_definition'].tolist()
            return {"word": input_word.capitalize(), "meaning": meanings}

        # Filter rows that contain the input word as a sub-word
        subword_matches = result[result['english_word'].str.lower() != input_word]
        if not subword_matches.empty:
            word_list = subword_matches['english_word'].tolist()[:5]
            meaning_list = subword_matches['malayalam_definition'].tolist()[:5]
            word_meaning_list = [{"word": word, "meaning": meaning} for word, meaning in zip(word_list, meaning_list)]
            return {"words": word_meaning_list}
    else:
        return {"message": "Word not found in dictionary"}
