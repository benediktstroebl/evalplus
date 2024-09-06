```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count
```

This script defines a function, `is_bored`, which takes a string as an input and counts the number of boredoms in the string. The function uses a generator expression along with the `sum` function to count the occurrences of boredoms. The script assumes that sentences are separated by any of the following punctuation marks: '.', '?', or '!'.