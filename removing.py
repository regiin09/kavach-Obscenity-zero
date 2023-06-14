import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')

# Define the Snowball stemmer for English
stemmer = SnowballStemmer('english')

# Define the list of stop words for English
stop_words = set(stopwords.words('english'))

def preprocess_text(text_content):
    # Convert the list of strings to a single string
    text = ' '.join(text_content)
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove non-alphanumeric characters
    text = ''.join(char for char in text if char.isalnum() or char.isspace())
    
    # Tokenize the text into words and phrases
    tokens = word_tokenize(text)
    
    # Remove stop words and stem the remaining words
    stemmed_tokens = [stemmer.stem(token) for token in tokens if token not in stop_words]
    
    # Rejoin the stemmed tokens into a single string
    processed_text = ' '.join(stemmed_tokens)
    
    # Return the processed text
    return processed_text
