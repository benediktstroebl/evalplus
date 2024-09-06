```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by periods to individualize sentences, and then trims any leading and trailing spaces from each sentence. Subsequently, it checks if each sentence starts with the word "I", and if it does, it increments the counter for boredoms. Ultimately, the function returns the count of boredoms.