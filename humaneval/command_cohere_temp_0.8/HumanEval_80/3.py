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

This Python script defines a function called `is_happy` that takes a single argument - a string of characters `s`. This function returns `True` if the string is "happy," and `False` otherwise. 

To be considered "happy," the string must have a length of at least 3 and each set of consecutive letters must be unique. The script utilizes a set, `letters_set`, to store and compare consecutive letters. 

The code checks each set of 3 consecutive characters in the string. If any set is not unique, the function returns `False`. If the length of the string is less than 3, it returns `False`. Otherwise, it returns `True`. 

This code can be used to efficiently determine whether or not a given string is "happy" according to the specified problem.