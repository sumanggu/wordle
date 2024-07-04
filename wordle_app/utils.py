import random

WORDLIST_PATHS = {
    'Run': 'wordle_app/static/Run.txt',
    'Start': 'wordle_app/static/Start.txt',
    'Fly': 'wordle_app/static/Fly.txt',
    'Jump': 'wordle_app/static/Jump.txt',
    'Master': 'wordle_app/static/Master.txt',
    'Walk': 'wordle_app/static/Walk.txt',
}

def get_random_word(wordlist_name):
    wordlist_path = WORDLIST_PATHS.get(wordlist_name)
    if wordlist_path:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            words = file.read().splitlines()
        return random.choice(words).strip()
    else:
        raise ValueError('Invalid wordlist name')




