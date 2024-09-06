```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach splits the input string by the delimiter '.' and loops through each sentence, checking various conditions to validate if it is a 'boredom' sentence as defined by the problem statement. The function returns the count of boredoms found in the given input string.