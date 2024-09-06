```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string by dot, trims whitespace from each sentence, and checks if the sentence starts with 'I'. If it does, it increments the counter, and returns the total count of boredoms.

You can easily test this function by calling it with different input strings.