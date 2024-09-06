```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            cnt += 1
    return cnt
```

This approach splits the input string by periods to individualize sentences, strips any trailing and leading whitespaces, and checks if the beginning word of each sentence is 'I'. Finally, it returns the count of sentences that start with 'I'.