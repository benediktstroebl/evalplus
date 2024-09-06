```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = sum(1 for sentence in S.split('. ') if sentence.startswith('I'))
    return boredoms
```

This function leverages Python's sum function and a generator expression to traverse each sentence and count the number of sentences that start with the word 'I'. This captures the essence of a boredom in the context of this prompt.