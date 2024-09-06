```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by periods to individualize sentences and then checks if the beginning of each sentence contains the word 'I'. The function returns the number of sentences that start with the word 'I'.