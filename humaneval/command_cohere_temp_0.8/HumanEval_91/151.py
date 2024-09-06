```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string `S` into a list of sentences using the period (`.`) as the delimiter. It then iterates through each sentence, trimming any leading or trailing white space with the `strip()` method. If a sentence starts with the word "I", it increments the counter `bored`. Finally, the function returns the count of sentences that match the "boredom" condition.