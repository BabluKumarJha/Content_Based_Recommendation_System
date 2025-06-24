# 🎬 Content-Based Movie Recommendation System

This is a content-based movie recommender system built using NLP techniques and cosine similarity to recommend movies based on user-selected titles. The app is deployed using **Streamlit** and fetches real-time movie posters from the **OMDb API**.
For similarity.pkl file you have to run code where we dump file. Because file size is more than 100 MB. While Github allow  only 25MB max size.
---

#### Kaggle Dataset:- https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

## 🚀 Features

- 📌 Clean NLP Pipeline (Tokenization + Stemming)
- 🧠 Content-Based Filtering (Using Genres, Cast, Director, Keywords, Overview)
- 🔍 Cosine Similarity with `CountVectorizer`
- 🎥 Poster Fetch via OMDb API
- 🖥️ Streamlit Web Interface
- 💾 Uses Pickle for Fast Inference

---

## 🛠️ Tech Stack

| Tool        | Purpose                      |
|-------------|------------------------------|
| Python      | Core Programming             |
| Pandas      | Data Handling                |
| NLTK        | Text Preprocessing (Stemming)|
| Scikit-learn| Vectorization + Similarity   |
| Streamlit   | Web UI for recommendations   |
| OMDb API    | Fetch movie posters          |

---

## 📁 Folder Structure

Content_Based_Recommendation_System/
│
📘 README.md                    # Project documentation
📓 Movie Recommendation System.ipynb  # Jupyter notebook (data prep + model)
🧠 movies_app.py               # Streamlit app script
📦 requirements.txt            # Python dependencies


## 📁 data                        
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
download:- Movies_metadata.csv and credits.csv.



---


## 📷 Screenshots

### 🔹 App Homepage
<img src="Screenshots/home.png" width="700"/>

### 🔹 Top 5 Recommendations
<img src="Screenshots/recommendations.png" width="700"/>

---

## 💡 How It Works

1. Load TMDB dataset and clean it.
2. Extract features: `overview`, `genres`, `keywords`, `cast`, `crew`.
3. Convert text into vectors using `CountVectorizer`.
4. Compute **cosine similarity** between vectors.
5. Recommend top 5 most similar movies to the selected one.
6. Use **OMDb API** to fetch movie posters by IMDb ID.

---

## 📦 Installation & Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/your-username/Content_Based_Recommendation_System.git
cd Content_Based_Recommendation_System



---

## 👤 Author

**Bablu Kumar Jha**

- 🔗 [GitHub](https://github.com/BabluKumarJha)
- 🧠 Passionate about Data Science, Machine Learning & AI
- 📊 Currently working on end-to-end ML projects with deployment


---

