```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script divides the given string `S` into separate sentences using the period ('.') as a delimiter. It then strips off the ending exclamation marks ('!') and question marks ('?') from each sentence. Next, it checks if the beginning word of each adjusted sentence is 'I'. If it is, then the sentence is considered a boredom, and the count is increased by one. The final count of boredom is then returned by the function. 

This solution adheres to the problem statement and provides an accurate count of boredom instances in the input string.