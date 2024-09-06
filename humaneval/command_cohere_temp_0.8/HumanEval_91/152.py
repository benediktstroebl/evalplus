```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    boredoms = 0
    for sentence in S.split('. ') + S.split('? ') + S.split('! '):
        if sentence.startswith('I '):
            boredoms += 1
    return boredoms
```

This approach splits the input string into sentences based on the punctuation marks ".", "?", and "!". Then it checks if each sentence starts with the word "I" to count the boredoms.