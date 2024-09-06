```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.'. Then, it iterates over each sentence, checks if it starts with the word 'I', and counts how many of these sentences exist. Finally, it returns the total count of boredoms.