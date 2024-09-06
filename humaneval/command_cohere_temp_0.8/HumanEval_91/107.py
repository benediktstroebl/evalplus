```python
def is_bored(S):
    count = 0
    sentences = S.split('.')
    for sentence in sentences:
        sentence = sentence.strip('?,!')
        if sentence.startswith('I'):
            count += 1
    return count
```

This approach splits the input string on '.' characters, stripping away any '?', '!' symbols that might still be attached to the ends of sentences. It then checks if the beginning of each sentence starts with the word 'I'.

The number of sentences that start with the word 'I' is counted and returned. Thus, giving you the number of "boredoms" in the input string.