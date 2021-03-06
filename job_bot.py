import praw
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    password='',
    user_agent='',
    username=''
)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    #Put new subreddits in here that you want to monitor for job postings
    subreddits = ["python", "haskell", "movies"]

    #Update the phrases that you want to look for in new job postings across your selected subreddits
    phrases_to_look_for = (
        "we are hiring", "we are looking for",
        "apply here", "hiring", "to apply",
        "remote opportunity")
    #Contains key-value pairs between Reddit post titles that are jobs/opportunities, and their URLS; each key-value pair is sent as part of an email to you, the user
    job_postings = {}

    for subreddit in subreddits:
        for thread in reddit.subreddit(subreddit).new(limit = 50):
            for phrase in phrases_to_look_for:
                if phrase in thread.selftext:
                    print(thread.title)
                    print(thread.url)
                    job_postings[str(thread.title)] = thread.url
    subject = 'Job postings from reddit bot'
    body = 'Latest job postings from subreddits: ' + str(subreddits)
    for job in job_postings:
        body += "\njob"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)




    