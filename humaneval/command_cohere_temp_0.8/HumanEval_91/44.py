```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script defines a function called `is_bored` that takes a string as an input and counts the number of boredoms in the string. A boredom is defined as a sentence that starts with the word "I". The function uses the split method to separate the input string into a list of sentences based on the delimiters '.', '?' or '!'. The strip method is used to remove these punctuation marks from the beginning and end of each sentence. The function then checks if each sentence starts with the word "I", and if it does, it increments the count of boredoms by one. Finally, the function returns the total count of boredoms in the input string.