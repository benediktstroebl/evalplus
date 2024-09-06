```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            count += 1
    return count
```

This approach splits the input string by the delimiter '.' and loops through each sentence. It checks if the sentence starts with the word 'I' and removes any exclamation points or question marks to ensure they are boredom sentences. The function returns the count of boredom sentences.