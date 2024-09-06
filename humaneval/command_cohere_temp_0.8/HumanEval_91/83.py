```python
def is_bored(S):
    count = 0
    sentences = S.split('.?!)'')
    for sentence in sentences:
        if sentence.strip()[0] == 'I':
            count += 1
    return count
```

This approach splits the string into a list of sentences based on the delimiters '.?!)' and then checks if the first character of each sentence is 'I'. The function returns the count of sentences that start with the word 'I'.