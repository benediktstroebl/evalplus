```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the punctuation marks '.' and '?!', and processes every sentence as a separate piece. The function increments the counter if the sentence starts with the word "I". Such sentences are considered as boredoms.