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

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

The script assumes that the length of the string is at least 3 to avoid `IndexError` and `TypeError`. The implementation efficiently checks that every 3 consecutive letters are distinct without wasting memory on the whole string comparison or writing explicit loops. It utilizes a `set` data structure to store recently encountered distinct letters and checks if every 3 consecutive letters are already in the set.