```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    bores = 0
    for sentence in S.split('. ') + S.split('? ') + S.split('! '):
        if sentence.startswith('I'):
            bores += 1
    return bores
```

This approach splits the input string into sentences based on common punctuation indicators ('.', '?', '!') and then checks if each sentence starts with 'I'. If it does, it counts up, and finally, returns the total count of boredoms. 

Note that the function assumes that the input string contains only lowercase alphanumeric characters and common punctuation indicators for sentence-splitting. You can adjust the function if you have specific requirements for the input format, providing additional preprocessing if needed.