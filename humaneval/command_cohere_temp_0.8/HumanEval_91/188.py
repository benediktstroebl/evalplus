```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach breaks the input string into a list of sentences using the period as a delimiter. It then iterates over each sentence, ignoring punctuation, and checks if the sentence starts with the word "I." If so, it increments the counter for boredoms. Finally, it returns the total count of boredoms found in the provided string.