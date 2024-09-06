```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(1, len(s) - 2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

The script defines a function `is_happy` that uses set manipulation to check if the conditions are met. This is done by creating a set of the first three letters, then checking if any of the subsequent two letters are in the set, ensuring that every 3 consecutive letters are distinct.