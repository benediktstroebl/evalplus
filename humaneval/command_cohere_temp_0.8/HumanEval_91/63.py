Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            cnt += 1
    return cnt
```

This function utilizes the **split('.')** method to separate the string into sentences and iterates through them using a loop. The **strip()** function is used to remove any leading or trailing spaces from each sentence. If a sentence starts with the word "I", it is considered a boredom and the count is incremented by 1. Finally, the function returns the total count of boredoms in the given input string.