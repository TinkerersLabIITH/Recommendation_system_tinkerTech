# Book & Movie Recommender Systems


This isn’t just a “project.” It’s a deployable, interactive recommendation engine you can launch in minutes. Built with real datasets and production-ready patterns — then wrapped in Streamlit for instant web deployment.

- **📚 Book Recommender** → Collaborative filtering. Suggests titles based on what *similar users* loved.  
- **🎬 Movie Recommender** → Content + metadata engine. Recommends based on *genre, cast, keywords* — no user history needed.

Plug it into your portfolio. Host it on Streamlit Cloud. Or tweak it into your startup’s MVP. No gatekeeping — just working code.

---

# 📦 Installation

## 1. **Get Python** — [python.org](https://www.python.org/downloads/)  
   *Check it works:*  
   ```bash
   python --version
```
## 2. **Clone this repo**
```bash
git clone https://github.com/yourusername/book-movie-recommenders.git
cd book-movie-recommenders
```

or just download the zip file by going to <>Code option and by selecting download through zip

## 3. **Install all the dependencies**
```bash
pip install -r requirements.txt
```

## 4.**Run the application** :)

    - Go to books_recommender_system.ipynb and run all the cells
    - Go to movies_recommender_system.ipynb and run all the cells
This would create a model directory with the following structure
```
model/
├── books.pkl
├── movie_list.pkl
├── popular.pkl
├── pt.pkl
├── similarity.pkl
└── similarity_scores.pkl
```

## 5. **Run your work**

For movie_recommender_system : 
```bash
streamlit run movies_recommender_system.py
```


For movies_recommender_system : 
```bash
streamlit run movies_recommender_system.py
```

For books_recommender_system:
```bash
streamlit run books_recommender_system.py
```

## Demo Videos
See it in action: 

**Movie Recommender**→ movies_recommender_system_demo.webm  

**Book Recommender** → streamlit-books_recommender_system_demo.webm 
     