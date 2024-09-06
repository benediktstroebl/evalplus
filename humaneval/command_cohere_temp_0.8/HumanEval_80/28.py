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

The problem is solved iterating through the string and checking if every group of 3 consecutive letters are distinct, and the happy function returns True or False accordingly. The function includes a check for the minimum length of the string, which is 3, to avoid any unexpected behavior for smaller inputs.