```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = sum(1 for sentence in S.split('.') + S.split('?') + S.split('!') if sentence.startswith('I'))
    return boredoms
```

This script splits the input string `S` into a list of substrings using punctuation marks '.'', '?'', and '!''. Then, it iterates over the substrings and checks if each one starts with the word 'I'. If it does, it counts it as a boredom and sums up the occurrences using the `sum()` function. Finally, the counted number of boredoms is returned as the function's result.