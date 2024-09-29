# Import required files

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests
import bz2file as bz2


# cosine is the cosine similarity array which we use to predict 
cosine = bz2.BZ2File('cosine.pbz2', 'rb')
cosine = pickle.load(cosine)

# k_neighbor is a machine learning model using which we predict
k_neighbor = bz2.BZ2File('k_neighbor.pbz2', 'rb')
k_neighbor = pickle.load(k_neighbor)

# Pivot is a data frame which contains all the book titles and the ratings given by the user
df = pd.read_csv('pivot.csv',index_col=0)
book_options = sorted(df.index.unique())
print(df.index)

# Book_isbn_all is a dataframe which contains the book title only stored in the pivot dataframe
# and its unique ISBN number
book_isbn = pd.read_csv('book_isbn.csv',index_col=0)
print(book_isbn.head)


# recommend_cosine function is used defined to predict
def recommend_cosine(book_name):
    # We find the index of a book using the pivot table
    index=np.where(df.index==book_name)[0][0]
    print(index)
    
    # The below command gives us the index and the closest distance to other books
    similar_items=sorted(list(enumerate(cosine[index])),key=lambda x:x[1],reverse=True)[1:11]
    print(similar_items)
    arr = []
    
    # Traverse through the array and get the book title of books to recommend
    for i in similar_items:
        book_title = df.index[i[0]]
        print(book_title)
        arr.append(book_title)
    return arr

# # recommend_k function is used defined to predict using k nearest neighbors
# def recommend_k(book_name):
#     # We find the index of a book using the pivot table
#     index=np.where(df.index==book_name)[0][0]
#     print(index)
    
#     # The below command gets the cloest distance and suggestion 
#     dist, sugg = k_neighbor.kneighbors(df.iloc[index, :].values.reshape(1,-1),n_neighbors=6)
#     print(dist)
#     print(sugg)
#     arr = []
#     for i in range(len(sugg[0])):
#         print(df.index[sugg[0][i]])
#         arr.append(df.index[sugg[0][i]])
#     return arr


# Details function which is responsible to fetch the details of the book using Google Book API
def details(book_name):
    # The below command returns an array containing ISBN numbers of a book
    # Note that a single book can have multiple ISBN numbers because of different publishers etc.
    arr = book_isbn[book_isbn['Book-Title'] == book_name]['ISBN'].to_list()
    for i in arr:
        print(arr)
        isbn = i
        api_key = 'Your_API_KEY_Here'
        url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={api_key}'
        response = requests.get(url)
        book = response.json()
        if response.status_code == 200:
            # Parse the JSON response
            books = response.json()
            print(len(books))
            # Loop through the results and print book titles and authors
            if books['totalItems']==0: # We're doing this incase there's no details in the API response
                continue
            else:
                for item in books['items']:
                    title = item['volumeInfo'].get('title', 'No Title')
                    authors = item['volumeInfo'].get('authors', ['No Author'])
                    categories = item['volumeInfo'].get('categories',['No Categories'])
                    description = item['volumeInfo'].get('description','No Description')
                    imagelinks = item['volumeInfo'].get('imageLinks', {}).get('thumbnail', 'https://www.corpstrat.com/wp-content/uploads/2022/05/istockphoto-1147544807-612x612-1.jpg')
                    print('Title:', title)
                    print(f'Authors: {", ".join(authors)}')
                    print(f'Categories: {", ".join(categories)}')
                    print('Description:', description)
                    print('Thumbnail:', imagelinks)
                    return [title,authors,categories,description,imagelinks]
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return []
    

# detail_arr = details('Grave Secrets')
# print(detail_arr)

def app():
    st.write("test")


st.title("Book Recommender System")

st.header('Recommend Books', divider='rainbow')  

option = st.selectbox("Type in your book", book_options,index=None,placeholder="Type Book...",)
st.write("You selected:", option)


if st.button("Recommend"):
    book_array = []
    book_array = recommend_cosine(option)
    
    tab_arr = ['Book '+str(i+1) for i in range(10)]
    st_arr = st.tabs(tab_arr)
    count = 0
    for i in range(10):
        with st_arr[i]:
            temp = book_array[i]
            st.subheader(temp,divider=True)
            detail_arr = details(temp)
            if detail_arr:
                st.write("Author: ",  " ".join(detail_arr[1]))
                st.write("Categories: ",  " ".join(detail_arr[2]))  
                st.write("Description: ",  detail_arr[3])  
                st.image(detail_arr[4], width=200)
            else:
                st.write("Failed to fetch data")
