from fastapi import FastAPI ,  Query
from fastapi.middleware.cors import CORSMiddleware
import json
from typing import List

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # Allow all origins
    allow_credentials=False,     # Credentials not allowed
    allow_methods=["GET"],       # Allow only GET requests
    allow_headers=["*"],         # Allow all headers
)

import json

# Load the data from names.json
with open("api/names.json", "r") as f:
    data = json.load(f)

# Convert list of dicts into a dict with name as key and marks as value
names_dict = {entry["name"]: entry["marks"] for entry in data}




@app.get("/api")
async def get_marks(name: List[str] = Query(None)):
    if not name:
        return {"error": "No names provided"}

    # Get marks for each provided name
    marks = [names_dict.get(n, 0) for n in name]
    return { "marks" : marks }
