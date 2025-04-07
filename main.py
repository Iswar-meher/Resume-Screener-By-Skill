import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load CSV file
df = pd.read_csv("Resume.csv")

# Clean text (lowercase, remove punctuation)
def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    return text

df["clean_resume"] = df["Resume_str"].apply(clean_text)

# Encode categories as numbers
le = LabelEncoder()
df["category_encoded"] = le.fit_transform(df["Category"])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["clean_resume"], df["category_encoded"], test_size=0.2, random_state=42
)

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Test accuracy
y_pred = model.predict(X_test_tfidf)
print("Accuracy:", accuracy_score(y_test, y_pred))

# ---- Predict on new input resume ----
resume_text = """
Experienced in Java, Spring Boot, and RESTful API development. Familiar with microservices and cloud deployment.
"""

# Clean and transform
resume_clean = clean_text(resume_text)
resume_tfidf = vectorizer.transform([resume_clean])

# Predict category
pred = model.predict(resume_tfidf)
category = le.inverse_transform(pred)
print("Predicted Category:", category[0])
