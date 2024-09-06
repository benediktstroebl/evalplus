Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This function iterates through every sentence, strips any leading and trailing whitespaces, and checks if the sentence starts with the word 'I'. If it does, it increments the counter. Finally, it returns the count of boredoms in the given input string. 

This solution adheres to the problem statement, and the provided code should work as expected. Feel free to test it with different inputs to observe how the function performs. Let me know if you need anything else!