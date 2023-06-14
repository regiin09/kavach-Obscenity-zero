from flask import Flask, render_template, request
import mysql.connector
from retreive import get_text_content
from removing import preprocess_text

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'R&sM^9h9RxXq3%',
    'database': 'words_cse'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/process', methods=['POST'])
def process_website():
    website = request.form.get('website')
    text_content = get_text_content(website)
    processed_text = preprocess_text(text_content)

    # Connect to MySQL database
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Perform the comparison and blocking logic
    offensive_words = get_offensive_words(cursor, processed_text)
    
    if offensive_words:
        # Perform blocking action or display a warning message
        result = 'Website is offensive. Blocked.'
        result += '\nOffensive words detected: ' + ', '.join(offensive_words)
    else:
        # Continue with the website
        result = 'Website is not offensive. Continue.'

    # Close the cursor and database connection
    cursor.close()
    cnx.close()

    return result

def get_offensive_words(cursor, text):
    # Perform a SELECT query to retrieve the offensive words present in the processed text
    query = "SELECT word FROM inappropriate_words WHERE word IN (%s)"
    values = ', '.join(['%s'] * len(text.split()))

    cursor.execute(query % values, tuple(text.split()))
    offensive_words = [row[0] for row in cursor]

    return offensive_words

if __name__ == '__main__':
    app.run()
