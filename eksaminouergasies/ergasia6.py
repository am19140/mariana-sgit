import instaloader
from collections import Counter

L = instaloader.Instaloader()
profile = input ("Enter an instagram profile: ")

insta = instaloader.Profile.from_username(L.context, profile)

data = []
for post in insta.get_posts():
    comments = post.get_comments()
    
    
    for comment in comments:      
        data.append(comment.owner.username)
    

   
       
C = Counter(data)
result = C.most_common(1)
print("Most frequent user in the comments is :", result)
