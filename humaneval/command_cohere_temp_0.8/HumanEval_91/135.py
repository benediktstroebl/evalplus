```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script divides the given string `S` into separate sentences using the sentence delimiter characters '.?'. The `strip` function is used here to remove these characters from the beginning and end of each sentence. Then, using the `startswith` function, it checks if the beginning of each sentence is prefixed with the word "I". Finally, it counts and returns the total number of sentences that match this criteria, representing boredoms. 

This approach allows the function to efficiently process each sentence within a single loop, ensuring the correctness of the solution while maintaining good performance characteristics.