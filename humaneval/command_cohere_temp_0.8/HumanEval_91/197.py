```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            cnt += 1
    return cnt
```

This approach splits the input string by periods to individualize sentences, and then trims any excess space. Using the `startswith` function, it checks if each sentence begins with "I", and if it does, it increments the counter. Finally, the function returns the count of sentences that resemble boredom.