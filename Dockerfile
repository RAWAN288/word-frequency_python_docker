# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and the text file into the container at /app
COPY word_freq.py /app/
COPY random_paragraphs.txt /app/

# Install any needed dependencies specified in requirements.txt
RUN pip install nltk

# Download NLTK data
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python", "word_freq.py" ,"/app/random_paragraphs.txt"]