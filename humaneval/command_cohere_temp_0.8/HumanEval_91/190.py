```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.' '?' or '!' and counts the number of sentences that start with the word "I". The function returns the total count of such sentences, representing the number of boredoms in the given input string.