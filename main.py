import random
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

# Load csv file
nba = pd.read_csv("Words.csv")



@app.get("/")    
async def root():
    # Generate 100 random numbers between 1 and 100
    random_numbers = random.sample(range(0, len(nba)), 5)
    #create a list of dictionary
    word_list = []
    for i in random_numbers:

        row_dict  = nba.loc[[i]].to_dict(orient='records')[0]
        word_list.append(row_dict )
        print(row_dict )
    return{"words": word_list}
