```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.'. Then, it checks if each sentence starts with the word 'I' and increments the counter if true. Finally, it returns the total count of boredoms.