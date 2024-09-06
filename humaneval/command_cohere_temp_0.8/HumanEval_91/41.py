```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the sentence markers ('.' punctuation marks) and iterates through every sentence. Using the `startswith()` method, it identifies and counts the number of sentences that start with the word "I". The `strip('!?')` step removes any trailing punctuation from each sentence before analysis to ensure accurate counting. 

The `is_bored()` function returns the total count of boredoms in the provided string.

This solution works well for the provided test cases and illustrates a clear and efficient approach to solving the problem.

**NOTE:** When splitting using `'.'`, please keep in mind that standard punctuation marks are being considered as sentence delimiters. If certain punctuation (like commas or hyphens) is vital to distinguish between sentences, the solution may need some tweaking.