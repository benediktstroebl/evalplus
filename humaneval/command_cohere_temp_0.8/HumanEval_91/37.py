```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.', '!?'. Then, it checks if each sentence starts with the word 'I', and increments the counter accordingly. Finally, it returns the total count of boredoms in the given input string.