```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i+1], s[i+2]])) != 3:
            return False
    return True
```

The function uses a simple algorithm to check every group of 3 letters in the string, if there is a group of 3 identical letters, it returns false. Otherwise, it checks all possible groups of 3 letters and returns True if they are all distinct. The function returns True if the condition is met and False otherwise.