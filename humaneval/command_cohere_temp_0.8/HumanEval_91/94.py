Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            count += 1
    return count
```

This script defines a function `is_bored` that takes a string as an input and counts the number of boredoms in the string. The function splits the string into a list of sentences using the sentence delimiter '.' and then counts the number of sentences that start with the word 'I' and end with either '.' '?' or '!' . Finally, the function returns the count of boredoms.