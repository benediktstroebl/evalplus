```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(3, len(s), 3):
        if len(set(s[i:i+3])) != 3:
            return False
    return True
```

This function checks whether the given string is happy by examining every successive group of 3 letters. The initial check ensures the string length is at least 3, after which every group of 3 letters is compared to ensure they are distinct. The function returns True if all groups of 3 letters are unique, and False otherwise. 

To use this function, you can simply call it by passing a string as an argument, and it will return True or False depending on whether the string is happy or not.