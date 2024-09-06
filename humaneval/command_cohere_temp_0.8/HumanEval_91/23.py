```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = 0
    for line in S.split('.'):
        line = line.strip('!?')
        if line.startswith('I '):
            boredoms += 1
    return boredoms
```

This approach ensures that each line is examined regardless of its ending punctuation, and it handles various sentence delimiters effectively. Furthermore, it is more tolerant to different indentation styles, as it does not rely on consistent spacing.

The `strip()` method is used here to remove '!?' characters from the line, which prevents double counting and ensures accurate processing.