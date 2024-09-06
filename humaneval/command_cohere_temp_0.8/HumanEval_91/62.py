```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredoms
```

This function uses a generator expression to iterate over different sentences in the string, classifying them by delimiter ('.', '?', or '!') and checking whether the sentence starts with the word 'I'. It then sums up the occurrences to provide the count of boredoms and returns the result.