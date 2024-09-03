```python
def is_bored(S):
    """
    Count the number of boredoms in a string of words. A boredom is a sentence 
    that starts with "I".
    """
    bored_count = 0
    sentence_start = True

    for c in S:
        if c == '.' or c == '?' or c == '!':
            sentence_start = True

        if sentence_start and c == 'I':
            bored_count += 1
            sentence_start = False

        if c == ' ':
            sentence_start = False

    return bored_count
```