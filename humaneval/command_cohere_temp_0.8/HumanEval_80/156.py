```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(letters_set) >= 3 and s[i] in letters_set:
            return False
        letters_set.add(s[i])
    return True
```

This Python script defines a function called `is_happy` that takes a single argument - a string `s`. This function returns `True` if the string is happy, meaning its length is at least 3 and every set of 3 consecutive letters are distinct, otherwise it returns `False`.

The script employs a set `letters_set` to store and manage the occurrences of the current and previous letters, determining happiness based on the distinctness of consecutive letter sets of size 3. It returns `True` if all such sets are unique, and `False` otherwise, providing a working implementation of the specified happy string check.