I have used tmdb_5000_movies abd tmdb_5000_credits csv datasets to create this project.

The process of development involved


1. data preprocessing
Initial preprocessing involves treating imbalanced data, null values and formatting the raw data or transforming into the required form.
Then the columns in movies dataset are concatenated with each other to form tags by selecting only required informations from the datasets.



2. vectorization
The datasets are transformed into vectors and then similarity index is generated which is between 0 and 1   



3. Front-end Development
   streamlit is used to create the frontend here in this application.


Note: similarity.pkl is not uploaded as it contains data exceeding 25 mb.
