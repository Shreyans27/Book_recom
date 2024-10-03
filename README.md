# Book Recommendation System (Collaborative-Based Filtering)

### Using K-Neighbor and Cosine Similarity
- Recommendation systems are taking over the world as so many websites and applications are using them as their fundamentals, some of which include famous companies like Amazon, Netflix, Youtube etc.
- One approach for recommendations systems is collaboraive filtering, which is a method that predicts based on what other users will recommend. Therefore it is basically a user-based filtering.
- For example lets say A and B both read a book and they both liked it. Now A also likes another book and will recommend it to B. This servers as the base of the technique.

### Machine Learning Model
1. **K - Nearest Neighbors (KNN)** algorithm is a supervised machine learning method for regression and classification problems.
    - The K-NN algorithm works by finding the K nearest neighbors to a given data point based on a distance metric, such as Euclidean distance. The class or value of the data point is then determined by the majority vote or average of the K neighbors. This approach allows the algorithm to adapt to different patterns and make predictions based on the local structure of the data.
    - The value of k is very crucial in the KNN algorithm to define the number of neighbors in the algorithm. The value of k in the k-nearest neighbors (k-NN) algorithm should be chosen based on the input data.
2. **Cosine Similarity** is a metric, helpful in determining, how similar the data objects are irrespective of their size.
    - In cosine similarity, data objects in a dataset are treated as a vector.
    - The cosine similarity is beneficial because even if the two similar data objects are far apart by the Euclidean distance because of the size, they could still have a smaller angle between them. Smaller the angle, higher the similarity.
  
### Dataset Link 
https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data

### Google Books API Link
https://developers.google.com/books/docs/overview

### Working Project Link
- **Note: The project hosted on streamlit won't showcase the API output because it is hosted via streamlit using github and I've removed my API key. However I've added images of the project hosted locally inlcuding the API responses.**
- https://book-recom.streamlit.app/

### Data Preprocessing
- All the data cleaning, preprocessing, model building, deploying etc. has been explained in the Jupyter Notebook uploaded above.

### How to Run Locally
1. Create a folder x and put all the below mentioned files in it.
    - book_recommender_main.py
    - book_top.csv
    - book_isbn_all.csv
    - create another folder with the name *pages* and put all the below mentioned files in it.
        - book_recommender.py
        - book_suggestor.py
        - pivot.csv
        - book_isbn.csv
        - book_isbn_all.csv
        - cosine.pbz2
        - k_neighbor.pbz2

2. Run the *book_recommender_main.py* file on spyder and open anaconda prompt.
3. Type ```streamlit run 'c:\users\admin\jupyter notebooks\projects\book_recom\book_recommender_main.py'``` on the anaconda shell to host locally

### Outputs
#### 1. Top Books Based on Rating
**Note that we're getting top books based on rating using the weighted average formula and it has been explained in the jupyter notebook**
![image](https://github.com/user-attachments/assets/8c100b73-896f-45c9-bcf1-5709d999e587)
![image](https://github.com/user-attachments/assets/dbc0fd69-7cbf-421e-81cf-67bda07203fd)
![image](https://github.com/user-attachments/assets/d0a92f2a-f28a-4823-8066-80bad06b1e5b)

  
