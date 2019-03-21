import praw

reddit = praw.Reddit('bot1', user_agent='bot1 user agent')
subreddit = reddit.subreddit('FortniteCompetitive+FortniteBR')

for submission in subreddit.stream.comments(skip_existing=True):
    print(submission.body)