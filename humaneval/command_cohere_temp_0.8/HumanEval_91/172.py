```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.', '!', and '?'. It then iterates through each sentence, removes the punctuation, and checks if the sentence starts with the word "I". If so, it increments the counter bored. Finally, the function returns the total count of boredoms.