**Project Title:** Movie Recommender System

**Objective:** The goal of this project is to create a system that provides users with recommendations for five movies closely related to a selected movie from a database of 5000 movies. By selecting a movie, the user will receive suggestions of other movies based on similarities in genres, keywords, cast, and crew.

**Approach:** The recommender system uses a combination of data analysis and machine learning techniques to generate movie recommendations. The dataset consists of two CSV files containing information about movies and their credits from the TMDB 5000 movies dataset on Kaggle. The data was merged and filtered down to a select few important columns: movie ID, title, genres, keywords, cast, and crew. A new 'tags' column was created by concatenating these features to form a comprehensive representation of each movie. This textual data was vectorized using `CountVectorizer`, and the cosine similarity was calculated to find the most similar movies to the user's selected choice.

**Data:** The dataset used in this project is the TMDB 5000 movies dataset from Kaggle, which includes details such as movie titles, genres, cast, and crew. The data was preprocessed by removing unnecessary columns, handling null values, and dropping duplicates.

**Expected Outcomes:** The desired result is to provide accurate and relevant movie recommendations to users based on their chosen movie. Success is measured by user satisfaction with the recommendations and the system's ability to match similar movies.

**Applications:** The user interface for the model is implemented using Streamlit, which allows users to input a movie name and receive recommendations directly within the application.
