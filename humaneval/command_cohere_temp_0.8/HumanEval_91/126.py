```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            bored += 1
    return bored
```

This approach splits the input string by the delimiter '.' and iterates over the resulting sentences. It uses `strip()` to clean the whitespace at the beginning and end of each sentence. If the sentence starts with the word 'I' and does not contain an exclamation mark or a question mark, it is considered a boredom and the counter is incremented. Finally, the function returns the count of boredoms.