```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the punctuation marks '.' and '!?', and then checks if the sentence starts with 'I', incrementing the counter accordingly. The `strip` method is used to remove these punctuation marks from the sentences, ensuring that they are not counted as part of the sentences for the boredom check.