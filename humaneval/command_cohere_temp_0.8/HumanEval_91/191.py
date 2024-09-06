Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This function iterates through each sentence in the input string, stripping out exclamation points and question marks that might delimit the end of a sentence. It then checks if the word following the trimming is "I", and if it is, it increments the counter. Finally, it returns the number of boredoms (sentences that start with "I") in the given string.