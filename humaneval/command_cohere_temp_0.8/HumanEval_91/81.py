Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.lower().startswith('i'))
    return boredom_count
```
This function uses a generator expression to iterate over each sentence (split by '. ' or '?' '!') and determines whether the sentence begins with the word "I" (case insensitive). It then sums up the occurrences to calculate the boredom count.