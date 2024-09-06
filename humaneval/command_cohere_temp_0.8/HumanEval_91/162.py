```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.strip()[0] == 'I')
    return boredom_count
```

This function uses a generator expression to iterate over each sentence (separated by '. ' as per the test cases) in the input string, and counts the number of sentences that start with the word 'I'. The sum() function then adds up these counts. The resulting count represents the number of boredoms in the given string.