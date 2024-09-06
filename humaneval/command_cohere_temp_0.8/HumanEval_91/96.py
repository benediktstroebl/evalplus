```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count
```

This script defines a function, `is_bored`, which takes a string as an input and counts the number of sentences that start with the word "I." The function uses the `sum` function to count the number of sentences that start with "I" from a list of split sentences (using '.', '?', or '!') that are generated from the input string. The total number of sentences meeting those criteria is then returned as the count of boredoms.