**MLOps Homework 2 - Email Classification**

## 📌 Overview
This project implements an **email classification API** using **Flask, Hugging Face transformers, and sentence embeddings**. The API dynamically loads classification labels from a file and allows users to **add new classes** via an endpoint.

---

## ✅ Features Implemented
- **Removes hardcoded classes** → Loads categories dynamically from `email_classes.txt`.
- **Allows adding new classes** → `/api/v1/add-class/` endpoint updates `email_classes.txt`.
- **Performs sentiment analysis** → `/api/v1/sentiment-analysis/` endpoint.
- **Fetches valid embeddings** → `/api/v1/valid-embeddings/` endpoint.
- **Classifies emails dynamically** → `/api/v1/classify/` endpoint.
- **Uses Flask API to expose the classification service**.

---

## 🛠️ Installation & Setup
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/mlops_hw2_email_classification.git
cd mlops_hw2_email_classification
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run the Flask App**
```bash
python app.py
```

✅ The API should now be running at `http://127.0.0.1:3000`.

---

## 📡 API Endpoints
### **1️⃣ Add a New Email Class**
#### `POST /api/v1/add-class/`
**Example Request:**
```bash
curl -X POST "http://127.0.0.1:3000/api/v1/add-class/" -H "Content-Type: application/json" -d '{"class_name": "Technology"}'
```
**Example Response:**
```json
{"message": "Class 'Technology' added successfully"}
```

### **2️⃣ Perform Sentiment Analysis**
#### `POST /api/v1/sentiment-analysis/`
**Example Request:**
```bash
curl -X POST "http://127.0.0.1:3000/api/v1/sentiment-analysis/" -H "Content-Type: application/json" -d '{"text": "I love AI and Machine Learning!"}'
```
**Example Response:**
```json
{"message": "Data received", "data": {"text": "I love AI and Machine Learning!"}, "sentiment": [{"label": "POSITIVE", "score": 0.98}]}
```

### **3️⃣ Retrieve Valid Embeddings**
#### `GET /api/v1/valid-embeddings/`
**Example Request:**
```bash
curl -X GET "http://127.0.0.1:3000/api/v1/valid-embeddings/"
```
**Example Response:**
```json
{"message": "Valid embeddings fetched", "embeddings": [...]} 
```

### **4️⃣ Classify an Email**
#### `POST /api/v1/classify/`
**Example Request:**
```bash
curl -X POST "http://127.0.0.1:3000/api/v1/classify/" -H "Content-Type: application/json" -d '{"text": "This email is about investment strategies."}'
```
**Example Response:**
```json
{"message": "Email classified", "classifications": [...]}
```

---

## 📂 Project Structure
```bash
mlops_hw2_email_classification/
│── app.py                 # Flask application
│── analyze.py             # Classification logic
│── requirements.txt       # Dependencies
│── email_classes.txt      # List of email categories (updated dynamically)
│── templates/
│   └── index.html         # Web interface (if needed)
```