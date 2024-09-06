```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredom_count
```

This script defines a function `is_bored` that takes a string as an input and counts the number of boredoms in the string. The function uses a combination of splitters (`!".?"`) to split the sentence into separate sentences and then checks if each sentence starts with the word "I". The sum() function is used to calculate the total count of boredoms in the input string.