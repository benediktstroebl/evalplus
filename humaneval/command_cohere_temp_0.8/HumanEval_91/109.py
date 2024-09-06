```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the sentence markers (`.` for simplicity), strips any leftover punctuation from the beginnings of these sentences, and then checks if the sentence starts with the word "I". The number of sentences starting with "I" is counted and returned. This should match the expected behavior from the problem statement.