```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count
```

This code defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. Boredoms are defined as sentences that start with the word "I". The function uses the `sum` function and a generating expression to count the number of boredoms in the string.

The summation iterates over the flattened list of substrings of `S` that are separated by punctuation marks '.', '?', or '!' – each substring corresponds to a sentence. Within the summation, a check is performed on each sentence to determine if it starts with the word 'I'. The function then returns the total count of boredoms in the input string.