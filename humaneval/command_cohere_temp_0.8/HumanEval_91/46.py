Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    cnt = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I') and sentence.find('!') == -1 and sentence.find('?') == -1:
            cnt += 1
    return cnt
```

This script defines a function `is_bored` that takes a string as an input and counts the number of boredoms in the string. The function splits the string into a list of sentences using the '.' delimiter and iterates over them. It checks if each sentence starts with the word "I" and does not contain any exclamation or question marks. If these conditions are met, it increments the count. Finally, the function returns the total count of boredoms.