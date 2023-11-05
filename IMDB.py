from imdb import Cinemagoer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pprint
#nltk.download('vader_lexicon')

#* Objective: Compare popular movie series's based on overall movie sentiment to find the most
#* family friendly option for movie night

ia = Cinemagoer() # open the movie database


# print(ia.search_movie("Harry Potter"))

print("\n\nBEGINNING\n\n")

# print(hp_movies[:10]) # Search IMDB for all Harry Potter related movies & # Gather movie IDs
hp1 = ia.get_movie("0241527",info = ["reviews"])
hp2 = ia.get_movie("0295297",info = ["reviews"])
hp3 = ia.get_movie("0304141",info = ["reviews"])
hp4 = ia.get_movie("0330373",info = ["reviews"])
hp5 = ia.get_movie("0373889",info = ["reviews"])
hp6 = ia.get_movie("0417741",info = ["reviews"])
hp7 = ia.get_movie("0926084",info = ["reviews"])
hp8 = ia.get_movie("1201607",info = ["reviews"])

hp1r = ia.get_movie("0241527")

"""
I tried using ChatGPT to find a way to pull the harry potter movie info into a dictionary containing
the movie title as the key and movie ID as the value to make this data aggregation scalable. It
recommended using the (re) library but it caused errors when I tried it so I just entered the info
manually :P
"""

def get_info(movie, info = 'reviews'):
    """
    collects movie info (default = reviews)
    """
    return movie.get(info, [])


def get_review_content(movie):
    """
    Returns the reviews for a specified movie
    """
    for review in movie:
        return(review['content'])

print (f"before{hp1r}")
hp1r = get_info(hp1r, 'rating')
print (f"after{hp1r}")

# for movie in range(len(hp_movies)):
#     movie = get_info(movie)
#     movie = SentimentIntensityAnalyzer().polarity_scores(get_review_content(movie))

# print(hp_movies)

hp1 = get_info(hp1)
hp2 = get_info(hp2)
hp3 = get_info(hp3)
hp4 = get_info(hp4)
hp5 = get_info(hp5)
hp6 = get_info(hp6)
hp7 = get_info(hp7)
hp8 = get_info(hp8)

# # Print reviews
# for review in hp1_r:
#     print(f"{review['content']}\n")


# print (get_review_content(hp1))

# for movie in hp_movies:


hp1_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp1))
hp2_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp2))
hp3_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp3))
hp4_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp4))
hp5_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp5))
hp6_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp6))
hp7_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp7))
hp8_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp8))



def del_dict_item(dict, item = 'compound'):
    """
    Removes the "compound" key from a dictionary
    """
    del dict['compound']
    return dict

x = 1
for dict in range(8):
    pass


# print(f"Title 1{hp1_score}")
# print(f"Title 2{hp2_score}")
# print(f"Title 3{hp3_score}")
# print(f"Title 4{hp4_score}")
# print(f"Title 5{hp5_score}")
# print(f"Title 6{hp6_score}")
# print(f"Title 7{hp7_score}")
# print(f"Title 8{hp8_score}")

hp1_score = del_dict_item(hp1_score)
hp2_score = del_dict_item(hp2_score)
hp3_score = del_dict_item(hp3_score)
hp4_score = del_dict_item(hp4_score)
hp5_score = del_dict_item(hp5_score)
hp6_score = del_dict_item(hp6_score)
hp7_score = del_dict_item(hp7_score)
hp8_score = del_dict_item(hp8_score)

harry_potter = [
    ('Harry Potter 1', hp1_score), ('Harry Potter 2', hp2_score), ('Harry Potter 3', hp3_score), ('Harry Potter 4', hp4_score), ('Harry Potter 5',hp5_score), ('Harry Potter 6', hp6_score), ('Harry Potter 7', hp7_score), ('Harry Potter 8', hp8_score)
]



# pprint.pprint(harry_potter)

neg_list = []
neu_list = []
pos_list = []
for title, sentiment in harry_potter:
    neg_list.append({sentiment['neg']:title})
    neu_list.append({sentiment['neu']:title})
    pos_list.append({sentiment['pos']:title})

neg_list_sorted = sorted(neg_list, key=lambda d: list(d.values())[0], reverse=True)
neu_list_sorted = sorted(neu_list, key=lambda d: list(d.values())[0], reverse=True)
pos_list_sorted = sorted(pos_list, key=lambda d: list(d.values())[0], reverse=True)

print("Negative values sorted:", neg_list_sorted)
print("Neutral values sorted:", neu_list_sorted)
print("Positive values sorted:", pos_list_sorted)

# print(hp1_score)

# for xxx in h
# pairs = [(score, sentiment) for sentiment, score in hp1_score.items()]
# print (pairs)



# d = dict()
# for sentiment, score in hp1_score.items():
#     for item in hp1_score.items():
#         d[score] = sentiment
# print (d)
# print(sorted(d))