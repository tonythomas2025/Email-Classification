import streamlit as st
import pickle

# Load the trained spam classifier
with open("spam_classifier.pkl", "rb") as model_file:
    spam_filter = pickle.load(model_file)

# Load the vectorizer
with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Streamlit App UI
st.title("📩 Spam Email Classifier")
st.write("Enter a message below to check if it's Spam or Not Spam.")

# User Input
user_input = st.text_area("Enter email/message:", "")

if st.button("Predict"):
    if user_input.strip():
        # Preprocess and transform input
        input_vectorized = vectorizer.transform([user_input])
        
        # Get classifier from pipeline
        classifier = spam_filter.named_steps['classifier']
        
        # Make prediction
        prediction = classifier.predict(input_vectorized)[0]

        # Debugging: Show prediction probabilities
        #probabilities = classifier.predict_proba(input_vectorized)
        #st.write("Prediction Probabilities:", probabilities)

        # Display Result
        if prediction == "spam":
            st.error("🚨 This message is **Spam**!")
        else:
            st.success("✅ This message is **Not Spam**.")
    else:
        st.warning("⚠️ Please enter a message first.")
