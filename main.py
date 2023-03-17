import praw
import json
import os

# replace the variables from lines 7-10 with your specific information

client_id = "your_id"
client_secret = "your secret"
subreddit = "relationship_advice" # use this or replace with your desired subreddit

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent="ios:python.finetune.ztmwork:v1 (fine-tuning lesson)",
)

data = []

submission_ids = []

for submission in reddit.subreddit(subreddit).top(limit=500):
    submission_ids.append(submission.id)
    
for id in submission_ids:
    submission = reddit.submission(id)
    title = submission.title
    print(title)
    submission.comments.replace_more(limit=0)
    data.append({
        'prompt': submission.selftext,
        'completion': submission.comments[1].body
    })

with open("reddit_data.jsonl", 'w') as f:
    for item in data:
        f.write(json.dumps(item) + "\n")
