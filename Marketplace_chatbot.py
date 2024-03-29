import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Download NLTK resources
#nltk.download('stopwords')

def convert_data_to_tuples(filename):
    
    """
      This function reads a JSON file containing intents data and returns a list of tuples
      combining intents and corresponding responses.

      Args:
          filename (str): The path to the JSON file.

      Returns:
          list: A list of tuples containing intents and responses.
    """
      # Read the JSON file
    with open(filename, "r") as f:
        data = json.load(f)

      # Initialize empty list to store tuples
    all_I = []

      # Loop through each greeting tag
    for tag in data:
        # Extract greetings and responses
        query = tag["patterns"]
        responses = tag["responses"]

        # Combine patterns and responses into tuples
        tuples = list(zip(query, responses))

        # Add tuples to the main list
        all_I.extend(tuples)

    return all_I

def respond_to_query(query, all_data):
    processed_query = preprocess_text(query)
    #print(processed_query)
    #print("\n\n")
    processed_responses = [preprocess_text(res) for res, _ in all_data]
    #print(processed_questions)    

    # Calculate Jaccard similarity for each question
    similarities = []
    for responses in processed_responses:
        if responses is not None:

            query_set = set(processed_query.split())
            responses_set = set(responses.split())
            intersection = len(query_set.intersection(responses_set))
            union = len(query_set.union(responses_set))
            if union != 0:
                
                similarities.append(intersection / union)  # Jaccard similarity score
            #else:
               # print("I'm sorry, I don't have an answer to that in my system")
    # Find the question with the highest similarity
    most_similar_index = similarities.index(max(similarities))

    # Check if similarity is above a certain threshold
    if similarities[most_similar_index] > 0.41:  # Adjust threshold as needed
        return all_data[most_similar_index][1]
    else:
        return "I'm sorry, I don't have an answer to that. Please wait while I connect you to a real person."

# Preprocess function example (replace with your actual implementation)
def preprocess_text(query):

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    word_list = word_tokenize(query.lower())

    words = [w for w in word_list if w not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]

    return ' '.join(words)

def main():
    while True:
        try:
            user_query = input("You: ")
            if user_query.lower() in ['exit', 'quit', 'goodbye', 'bye']:
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = respond_to_query(user_query, all_data)
            print("Chatbot:", response)
        
        except KeyboardInterrupt:
            print("\nChatbot: Bye! See you next time. (interrupted)")
            break
        
filename = "intents_file.json"  # Replace with your actual file name
all_data = convert_data_to_tuples(filename)
        
if __name__ == "__main__":
    print("To finish the chat please type:\n\t exit or quit or goodbye or bye ")
    main()
