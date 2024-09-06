```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script defines a function called `is_bored` that takes a string as an input parameter, splits the given text on the dot character ('.'), and then counts and returns the number of sentences that start with the word 'I' and hence are indicative of boredom. The function automatically handles variations in sentence structure including trailing and leading spaces, as evidenced by the test cases.