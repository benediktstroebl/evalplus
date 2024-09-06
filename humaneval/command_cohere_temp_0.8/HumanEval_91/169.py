```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach splits the input string by the sentence markers '.' and iterates over every sentence. For every sentence, it checks if it starts with the word 'I' and does not end with an exclamation mark or a question mark to count the boredoms.