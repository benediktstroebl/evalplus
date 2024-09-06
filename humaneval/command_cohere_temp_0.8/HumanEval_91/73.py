```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach breaks the input string into separate sentences by splitting it at each period (`.`) and then checks if each sentence starts with the word "I". The `strip()` function is used to remove any leading or trailing whitespace from each sentence, ensuring that the check for "I" is case-insensitive. The function returns the count of sentences that match the criteria.