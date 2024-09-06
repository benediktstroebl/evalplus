```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count
```

This code defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. A boredom is a sentence that starts with the word "I". The code uses a sum function with a generator expression to count the number of boredoms. The generator expression concatenates the string `S` with the delimiter characters `.`, `?`, and `!` to split `S` into sentences and checks if the start of each sentence is "I". The result is the count of boredoms in the input string.