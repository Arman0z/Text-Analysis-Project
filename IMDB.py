from imdb import Cinemagoer
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.download('vader_lexicon')

#* Objective: Compare popular movie series's based on overall movie sentiment to find the most
#* family friendly option for movie night

ia = Cinemagoer() # open the movie database


hp_movies = ia.search_movie("Harry Potter")

# print(hp_movies[:10]) # Search IMDB for all Harry Potter related movies & # Gather movie IDs
hp1 = ia.get_movie("0241527", info = ["reviews"])
hp1 = hp1.get('reviews', [])
hp2 = ia.get_movie("0295297",info = ["reviews"])
hp2 = hp2.get('reviews', [])
hp3 = ia.get_movie("0304141",info = ["reviews"])
hp3 = hp3.get('reviews', [])
hp4 = ia.get_movie("0330373",info = ["reviews"])
hp4 = hp4.get('reviews', [])
hp5 = ia.get_movie("0373889",info = ["reviews"])
hp5 = hp5.get('reviews', [])
hp6 = ia.get_movie("0417741",info = ["reviews"])
hp6 = hp6.get('reviews', [])
hp7 = ia.get_movie("0926084",info = ["reviews"])
hp7 = hp7.get('reviews', [])
hp8 = ia.get_movie("1201607",info = ["reviews"])
hp8 = hp8.get('reviews', [])


"""
I tried using ChatGPT to find a way to pull the harry potter movie info into a dictionary containing
the movie title as the key and movie ID as the value to make this data aggregation scalable. It
recommended using the (re) library but it caused errors when I tried it so I just entered the info
manually :P
"""
# # Print reviews
# for review in hp1_r:
#     print(f"{review['content']}\n")

def get_review_content(movie):
    """
    Returns the reviews for a specified movie
    """
    for review in movie:
        return(review['content'])
    
# print (get_review_content(hp1))

hp1_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp1))
hp2_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp2))
hp3_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp3))
hp4_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp4))
hp5_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp5))
hp6_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp6))
hp7_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp7))
hp8_score = SentimentIntensityAnalyzer().polarity_scores(get_review_content(hp8))

print(f"Title 1{hp1_score}")
print(f"Title 2{hp2_score}")
print(f"Title 3{hp3_score}")
print(f"Title 4{hp4_score}")
print(f"Title 5{hp5_score}")
print(f"Title 6{hp6_score}")
print(f"Title 7{hp7_score}")
print(f"Title 8{hp8_score}")


d = dict()
for sentiment, score in hp1_score.items():
    for item in hp1_score.items():
        d[item] = score, sentiment

print (d)