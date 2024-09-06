```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('?')
        if sentence.startswith('I'):
            boredoms += 1
    return boredoms
```

This script splits the input string by punctuation marks '.' and iterates through the resulting words. It counts the number of sentences that start with the word "I" and assigns them to the variable `boredoms`. Finally, it returns the variable `boredoms` which contains the number of boredoms. 

Note that this approach assumes that sentences in the input string are separated by periods.