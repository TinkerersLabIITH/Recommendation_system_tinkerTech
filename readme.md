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





## 3. **Set Up Python Virtual Environment & Install Dependencies**  

To run this project smoothly, it’s recommended to use a **virtual environment**. Follow one of the two methods below:  

---

### 🔹 Option 1: Using Terminal (Recommended)  

```bash
# Create a new virtual environment (name it 'venv' or anything you like)
python -m venv venv  

# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate  

# Install all required packages
pip install -r requirements.txt
```

Or

### 🔹 Option 2: Using Jupyter Notebook  

1. Open the `.ipynb` notebook.  
2. On the **top-right corner**, click the **kernel selection dropdown**.  
3. Choose **“Add Environment”** → select **Python environment**.  
4. When prompted, provide the path to your installed Python interpreter:  
   - Example (Windows):  
     ```
     C:\Users\<YourName>\AppData\Local\Programs\Python\Python39\python.exe
     ```
   - Example (Mac/Linux):  
     ```
     /usr/local/bin/python3
     ```  
5. Once the environment is created, Jupyter will suggest installing the required packages.  
6. Install them using the suggested option, or manually run:  

   ```bash
   pip install -r requirements.txt
   ```

4.**Run the application** :)

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

### 🎬 Movie Recommender

Watch Demo Video

[movies_recommender_system_demo.webm](https://github.com/user-attachments/assets/8547fc42-1ab7-4d37-ad1c-74109d3f3852)



### 📚 Book Recommender

Watch Demo Video

[books_recommender_system_demo.webm](https://github.com/user-attachments/assets/6add97d9-0dd6-4dd3-80e8-6e83b0fd7449)


