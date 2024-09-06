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

The problem asks us to determine whether a given string is "happy" or not. A string is considered happy if its length is at least 3 and every set of 3 consecutive letters are distinct. This script defines a function `is_happy` which utilizes set comprehension to efficiently check if every set of 3 consecutive letters is unique.