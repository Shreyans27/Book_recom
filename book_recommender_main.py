# Import required files

import streamlit as st
import numpy as np
import pandas as pd
import pickle
import requests
import bz2file as bz2


# Book_top is a sorted dataframe which contains the top books which are sorted by the weighted average
# of the rating column
df = pd.read_csv('book_top.csv',index_col=0)
book_options = sorted(df.index.unique())
print(df.index)

# Book_isbn_all is a dataframe which contains the book name and its unique ISBN number
book_isbn_all = pd.read_csv('book_isbn_all.csv',index_col=0)
print(book_isbn_all.head)


# Details function which is responsible to fetch the details of the book using Google Book API
def details(book_name):
    # The below command returns an array containing ISBN numbers of a book
    # Note that a single book can have multiple ISBN numbers because of different publishers etc.
    arr = book_isbn_all[book_isbn_all['Book-Title'] == book_name]['ISBN'].to_list()
    for i in arr:
        print(arr)
        isbn = i
        api_key = 'Your_Key_Here'
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


st.set_page_config(
    page_title = "Home",
    )

st.title("Book Recommender System")

st.header('Top Books by Rating', divider='rainbow')   

# Find the top 10 books
book_array = df['Book-Title'].to_list()[:10]

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
