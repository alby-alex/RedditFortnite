import praw


def main():
    reddit = praw.Reddit('bot1', user_agent='bot1 user agent')
    subreddit = reddit.subreddit('FortniteCompetitive+FortniteBR')

    for submission in subreddit.stream.comments(skip_existing=True):
        if ("!stats" in submission.body):
            giveResponse(submission)


def giveResponse(s):
    import stats
    save = s.body
    k = save.index("!stats")
    save = save[k + 6:]
    save = save.strip()
    list = stats.stats(save)
    if (list is None):
        s.reply("No user found with name: " + save)
    else:
        s.reply(
            "Stats for username: " + save + "\n\n\nWins: " + list[0] + "\n\n\nWin Percentage: " + list[1] + "\n\n\nK/D: " + list[
                3] + "\n\n\nTotal Kills: " + list[
                2] + "\n\n\n\n\n\n\n\n\nThis is a bot providing a service. ")


main()
