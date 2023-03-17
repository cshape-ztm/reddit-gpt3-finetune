# Fine-Tuning a GPT-3 model from Reddit Data

This repository contains a Python script (main.py) which can take data from the reddit API and turn it into a JSONL file of prompt/completion pairs which can be used to fine-tune a GPT3 model. The prompts are post titles and the completions are the top comments.

This tool requires a bit of command line/terminal usage - if you have no experience with that, don't worry as you should be able to follow along just fine.

# Requirements

- Python3 installed on your computer
- An OpenAI account with the [command-line interface installed](https://platform.openai.com/docs/guides/fine-tuning)
- A [reddit application](https://www.reddit.com/prefs/apps) (don't worry this just takes a moment to create)

# Instructions

### Getting the Reddit Data and creating the JSONL File

1. Note down the `client_id` and `client_secret` from your reddit application
2. In the `main.py` file, replace the values in lines 7, 8, and 9 with your reddit application credentials and the target subreddit
3. Install [praw](https://praw.readthedocs.io/en/stable/getting_started/installation.html). Usually this means navigating to the folder with the `main.py` file in the terminal and entering `pip install praw` or `pip3 install praw`
4. Run the script. Usually this means entering `python main.py` or `python3 main.py`

This will produce a JSONL file of prompt/completion pairs in the folder with the `main.py` script.

### Using the JSONL File to Fine-Tune a GPT3 Model

1. In the terminal, enter `openai tools fine_tunes.prepare_data -f reddit_data.jsonl`
2. Answer `y` to all of the prompts
3. Take note of the suffix separator and suffix ending
4. In the terminal, enter `openai api fine_tunes.create -t reddit_data_prepared.jsonl`

Congratulations! Your fine-tuning job will now be started by OpenAI!

It will take awhile (minutes or hours, generally) for the job to complete. If the stream is interrupted, don't worry as the job will continue. You can check the status of the job by entering `openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>`.

Once completed, you can use the fine-tuned model via API or in the playground.

