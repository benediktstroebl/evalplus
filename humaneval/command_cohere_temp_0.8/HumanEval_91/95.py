Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I ') or sentence.startswith('i '):
            boredoms += 1
    return boredoms
```

This script defines a function `is_bored` that takes a string as an input and counts the number of boredoms in the given string. The function iterates over each sentence using the `split()` method, and for each sentence, it uses the `startswith()` method to check if the sentence starts with the word "I". If it does, it increments the count of boredoms. Finally, the function returns the total count of boredoms in the input string.