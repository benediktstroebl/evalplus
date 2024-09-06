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

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function first checks if the length of the string is at least 3, and if not, it returns `False`. If the string length is at least 3, it then checks if every 3 consecutive letters are distinct. It does this by using a `set` to keep track of the letters encountered, if every group of 3 yields a set of size 1, then it returns `False`, otherwise, it returns `True`. The script addresses the examples outlined in the problem statement and should generally be modified to tackle edge cases and improve robustness.