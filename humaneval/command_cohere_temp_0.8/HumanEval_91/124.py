```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.' '!' and '?'. Then, it iterates over each sentence and uses the startswith method to check if each sentence starts with the word 'I'. If it does, it increments the counter bored. Finally, the function returns the total count of boredoms.