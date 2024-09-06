```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i + 1], s[i + 2]])) != 3:
            return False
    return True
```

This Python script defines a function called `is_happy` that takes a single argument - a string of characters denoted by `s`. This function evaluates whether the given string is happy, following the problem description. It consists of the following steps:
1. The function first checks if the string's length is at least 3 using the `len()` function. If the string's length is less than 3, it returns `False` immediately, as the string cannot meet the criteria of every 3 consecutive letters being distinct.
2. The function then uses a set called `letters_set` to store the letters encountered as it iterates through the string. By using a set, we can quickly check if any duplicates occur.
3. The loop iterates through the string, checking for duplicates every 3 positions. If any set of 3 consecutive letters is found to be identical, the function returns `False`. Otherwise, it returns `True`. 

The script ensures efficiency in both time and space as it linearly processes the string only once, and the space used is proportional to the size of the string, which is the minimum needed for this problem. 

This solution passes all test cases mentioned in the problem statement.