# reddit-job-finder
This is my first simple reddit bot. I did it to learn about Python and PRAW.
This bot scans subreddits designated by the user for any new job/opportunity postings; it uses a list of keywords/phrases to identify whether or not a post is a job/opportunity. It then sends an email to the user about all the job postings it could find.

Why?
-----
In many subreddits, flairs are not enough to be able to find jobs; people end up posting without paying attention to the subreddit rules, and just post jobs. Also, many subreddits where job offers are posted don't have designated flairs for jobs in the first place. This makes it hard to know programatically what is and isn't a job or opportunity.
My idea was to go through a subreddit, filter posts by "New", and check if the body of a post submission matched with any keyphrases that you would normally see with a job listing (eg. "we are hiring for...", "a new opportunity just opened up...", etc.). 
I wanted to conveniently send myself these job offers, so I used smtplib to sign in to my Gmail account, and send an email to myself with all the job postings that the reddit bot would be able to find.

How do I use this for myself?
-----------------------------
If you want to install this on your own computer and get it running locally, you would need to:
- **Install PRAW** (this is a Python API that lets you talk to Reddit)
- Configure your CLIENT_ID, CLIENT_SECRET, REDDIT_PASSWORD, USER_AGENT, REDDIT_USERNAME, EMAIL_USER, and EMAIL_PASS environment varibales
- Make changes on lines 24 and 27, to update what subreddits and phrases you want to mix and match for your job finding.
- Run the bot by doing: python3 job_bot.py
