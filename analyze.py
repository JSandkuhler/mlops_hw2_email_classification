from transformers import pipeline
from sentence_transformers import SentenceTransformer
import numpy as np
import os

sentiment_pipeline = pipeline("sentiment-analysis")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

CLASS_FILE = "email_classes.txt"

# Function to load email classes from a file
def load_email_classes():
    if not os.path.exists(CLASS_FILE):
        default_classes = ["Work", "Sports", "Food"]
        with open(CLASS_FILE, "w") as f:
            f.write("\n".join(default_classes))
    with open(CLASS_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

EMAIL_CLASSES = load_email_classes()

def get_sentiment(text):
    response = sentiment_pipeline(text)
    return response

def compute_embeddings(embeddings = EMAIL_CLASSES):
    embeddings = model.encode(embeddings)
    return zip(EMAIL_CLASSES, embeddings)

def classify_email(text):
    # Encode the input text
    text_embedding = model.encode([text])[0]
    
    # Get embeddings for all classes
    class_embeddings = compute_embeddings()
    
    # Calculate distances and return results
    results = []
    for class_name, class_embedding in class_embeddings:
        # Compute cosine similarity between text and class embedding
        similarity = np.dot(text_embedding, class_embedding) / (np.linalg.norm(text_embedding) * np.linalg.norm(class_embedding))
        results.append({
            "class": class_name,
            "similarity": float(similarity)  # Convert tensor to float for JSON serialization
        })
    
    # Sort by similarity score descending
    results.sort(key=lambda x: x["similarity"], reverse=True)
    
    return results