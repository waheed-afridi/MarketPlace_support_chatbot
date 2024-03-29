# MarketPlace_support_chatbot
### The chatbot is designed to provide responses to user queries based on predefined intents and responses stored in a JSON file. It utilizes natural language processing (NLP) techniques to preprocess user queries and calculate the similarity between the queries and the predefined intents.

## Requirements:
- python3
- nltk 
```bash
pip install nltk
```

## Cloning:
clone this repository by running the following links one by one in command prompt for window.
```bash
git clone https://github.com/waheed-afridi/MarketPlace_support_chatbot
```
```bash
cd MarketPlace_support_chatbot
```
```bash
python python Marketplace_chatbot.py
```

## Specificatoin:
- Responds to user queries using pre-defined intents (questions) and responses.
- Jaccard similarity finds the closest matching response.
- Handles exit commands ("exit", "quit", "goodbye", "bye") .
- This is a command-line chatbot, meaning the user interacts with it by typing queries and the responses are displayed on the console.
- It should handle user typos and variations in phrasing to some extent (due to the use of word stemming/lemmatization).
- The chatbot should gracefully handle situations where no close match is found in the dataset.
- The code is written in Python and requires the following libraries:
1. json
2. nltk (with stopwords, word_tokenize, and WordNetLemmatizer functionalities downloaded)

## Architecture:
- Data Layer:
  - JSON file containing intents data (questions and corresponding responses).
- Processing Layer:
  - convert_data_to_tuples function: Reads the JSON file and converts it into a list of tuples (questions, responses).
  - preprocess_text function (replace with your actual implementation): Performs text preprocessing on user queries and response patterns (questions) from the dataset (e.g., removing stop words, lemmatization).
  - respond_to_query function: Takes a user query and the dataset (list of tuples) as input. It preprocesses the query, calculates Jaccard similarity between the query and each response pattern, finds the closest match based on similarity, and returns the corresponding response from the dataset.
 
- Interaction Layer:
  - main function: Runs the main chat loop, handling user input, calling respond_to_query to get responses, and printing chatbot responses. It also handles exit commands ("exit", "quit", "goodbye", "bye").

- Data Flow:
  - User enters a query through the command-line interface.
  - The main function captures the user query.
  - The respond_to_query function is called with the user query and the dataset (list of tuples).This function preprocesses the user query and response patterns (questions) from the dataset. It calculates Jaccard similarity between the query and each response pattern. It finds the closest match based on similarity.
  - The respond_to_query function returns the corresponding response from the dataset or a message suggesting human assistance if no close match is found.
  - The main function displays the chatbot's response to the user.
