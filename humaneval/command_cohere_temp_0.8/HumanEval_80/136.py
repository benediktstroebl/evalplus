```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    if len(letters_set) == 3 and all(s[i:i+3].count(c) <= 1 for i in range(0, len(s) - 2, 3) for c in letters_set):
        return True
    else:
        return False
```

The problem asks us to determine if a string is happy or not based on two conditions:
1. The length of the string must be at least 3 to have three consecutive letters.
2. Every set of three consecutive letters must be unique. 

The script initializes an empty set to store the first three letters of the string. The uniqueness of consecutive letters is checked using nested list comprehensions. The `any` function returns `True` if any of the nested conditions evaluate to True, implying that at least one set of three consecutive letters is not unique, and the function returns `False`. The corresponding tests for the happy string are `is_happy('abcd')` and `is_happy('adb')`, which trigger the true branch and return True. 

The case where the string is not long enough or where the letters are not unique is handled by the initial checks on the length and the set, returning the opposite result. 

This solution could have been improved by implementing memoization to avoid the nested list comprehension and simplify the code.