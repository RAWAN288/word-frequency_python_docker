import nltk
from nltk.corpus import stopwords
from collections import Counter
nltk.download('punkt')
nltk.download('stopwords')
def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    return filtered_tokens
def count_word_frequency(tokens):
    word_freq = Counter(tokens)
    return word_freq

with open("random_paragraphs.txt", "r") as file:
    # Read the contents of the file
    text = file.read()

# Preprocess the text
processed_tokens = preprocess_text(text)

# Count word frequency
word_freq = count_word_frequency(processed_tokens)

# Display word frequency count
print("Word Frequency Count:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")

# Sort word frequency dictionary by frequency in descending order
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

# Display the top 100 most common words
print("Top 100 Most Common Words:")
for i, (word, freq) in enumerate(sorted_word_freq[:100], 1):
    print(f"{i}. {word}: {freq}")
