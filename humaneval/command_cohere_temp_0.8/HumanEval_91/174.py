```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('?')
        if sentence.startswith('I'):
            boredoms += 1
    return boredoms
```

This approach splits the input string on periods, strips off trailing question marks (if any), and checks if the resulting string starts with the word "I". If it does, it counts those sentences as "boredoms". The function returns the total count of boredoms in the given input string. 

The problem statement also mentions test cases, but they are not provided in the docstring or the code. If you could provide those test cases, I can add a comprehensive test suite to ensure the correctness of our solution and improve its reliability.