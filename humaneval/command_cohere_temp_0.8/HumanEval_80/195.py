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

This Python script defines a function called `is_happy` that takes a single argument - a string of characters `s`. This function returns `True` if the string is "happy", and `False` otherwise. 

The function first checks if the length of the string is at least 3, and if it is not, it returns `False`. This is the basic requirement for a string to be considered "happy".

If the string length is at least 3, the function then iterates through the string, but without checking the last two characters, as these would already have been checked in the previous step. In the loop, the function collects 3 consecutive characters at a time and checks if the set of these 3 consecutive characters is of size 3. If it is not, the function returns `False` as these consecutive letters are considered "happy" only if they are distinct. The function returns `True` if all sections are "happy". 

The script passes the test cases provided in the original problem description and is suitable for use in a markdown cell.