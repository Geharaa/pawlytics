# Pawlytics

AI-Based Pet Behavior Analysis System Using NLP and Machine Learning

## Summary

Pawlytics is a pet behavior-analysis system that helps owners interpret what they observe in their pets. An owner describes their pet's behavior or symptoms in everyday language, and Pawlytics uses Natural Language Processing (NLP) and Machine Learning to classify the description into a health-related category, returning a possible cause, a confidence score, and a recommended action with an urgency level. By turning unstructured behavioral observations into structured, data-driven insight, and by building a time-stamped behavior history for each pet, Pawlytics aims to support earlier detection of potential health issues and give veterinarians more reliable historical records to work from. It provides supportive insights only and is not a substitute for professional veterinary diagnosis.

## Tech Stack

**Backend:** Python (FastAPI), REST API with authentication and data validation

**Frontend / Dashboard:** React.js web interface (Streamlit used for early prototyping)

**Machine Learning & NLP:** scikit-learn (classical models), HuggingFace & sentence-transformers (embeddings/transformers), spaCy / NLTK (text preprocessing); models developed and trained in Google Colab

**Data handling & visualization:** pandas, NumPy, Matplotlib

**Database:** PostgreSQL (Supabase / Neon)

**Tooling:** GitHub (version control), VS Code, Jupyter Notebook / Google Colab

## Project Structure

```
pawlytics/
├── backend/        # FastAPI application
│   ├── app/
│   │   ├── models/
│   │   ├── routers/
│   │   └── main.py
│   └── requirements.txt
├── ml/             # Notebooks & datasets for model development
│   ├── notebooks/
│   └── data/
├── frontend/       # Web UI (to be built in Phase 4)
├── docs/           # Proposal and design documentation
└── README.md
```

## Project Status

Phase 1 — design & setup in progress
