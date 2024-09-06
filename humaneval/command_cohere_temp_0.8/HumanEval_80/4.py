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

This Python script defines a function called `is_happy` that takes a single argument - a string of characters denoted by `s`. This function evaluates whether the given string is happy, following the problem description. It consists of the following steps:
1. The string must have a minimum length of at least 3 characters.
2. It checks if each set of consecutive triplets of letters are distinct.

The function returns `True` if the given string `s` is happy, and `False` otherwise. You can use this function to check if any given string is happy or not, as described in the provided problem statement. 

To test this function, you can use the following examples:
```python
print(is_happy("abcd"))  # Output: True
print(is_happy("aabb"))  # Output: False
print(is_happy("adb"))  # Output: True
print(is_happy("xyy"))  # Output: False
```

These examples test various cases to ensure the function follows the happy string criteria.