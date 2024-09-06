```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach breaks the input string into separate sentences by splitting it based on the '.' character. It then strips any exclamation marks or questions marks from the end of each sentence to ensure accurate counting. After preparation, each sentence is checked if it starts with the word 'I', and if it does, it counts it as a boredom. Finally, it returns the total count of boredoms found in the given input string.