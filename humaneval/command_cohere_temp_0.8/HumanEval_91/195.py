```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the punctuation marks '.' and '!?'. The '?' and '!' are treated as single characters using the `strip()` method. Then for each sentence, it checks whether the sentence starts with the word "I", and increments the counter if so. Overall, the `is_bored` function returns the number of sentences that start with the word "I".