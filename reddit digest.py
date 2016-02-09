import praw
import os
import webbrowser
import dominate
from dominate.tags import *

subreddit_list = ['news', 'aww', ]      # Insert your subreddits here
post_list = []
new_list = []

r = praw.Reddit(user_agent='getter')
for i in subreddit_list:
    j = r.get_subreddit(i)
    post_list.append(j.get_top_from_week())

for j in post_list:
    for i in j:
        new_list.append([i.permalink, i.ups, i.title, i.domain])
        
sorted_list = sorted(new_list, key=lambda x: x[1], reverse=True)

doc = dominate.document(title='Reddit Digest')

with doc.head:
    link(rel='stylesheet', href='https://cdn.jsdelivr.net/min/1.5/min.min.css')
    script(type='text/javascript', src='script.js')

with doc:
    with div(id='container').add(ul()):
        for item in sorted_list:
            li(a(str(item[1]).encode('ascii', 'ignore') + '  -  ' + item[2].encode('ascii', 'ignore'), href=item[0].encode('ascii', 'ignore')))

path = os.path.abspath('temp.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(str(doc))
webbrowser.open(url)
