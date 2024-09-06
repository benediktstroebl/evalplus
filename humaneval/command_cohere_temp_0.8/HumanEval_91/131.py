```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count
```

This code defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. A boredom is a sentence that starts with the word "I". The function uses the `sum()` function to count the number of sentences that start with the word "I" by using a list comprehension that iterates over the split sentences (using split delimiter characters '.', '?', and '!') and checks if the beginning of each sentence is "I".