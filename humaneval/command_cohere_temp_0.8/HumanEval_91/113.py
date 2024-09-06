```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script defines a function called `is_bored` that takes a string as an input parameter, and counts the number of boredoms in the string. A boredom is defined as a sentence that starts with the word "I". The function uses string splitting and stripping techniques to analyze the input string and identifies boredoms as described in the problem statement. Finally, the function returns the number of boredoms found in the input string.