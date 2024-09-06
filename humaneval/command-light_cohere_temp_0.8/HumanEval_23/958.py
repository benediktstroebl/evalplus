Here's the corrected and self-contained version of the Python script that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Testing the function
>>> strlen('')
0
>>> strlen('abc')
3
>>> strlen('')abc')
3
>>> strlen('abcabc')
5
>>> strlen('hello world!')
11
>>> strlen('00000000')
0
``` 
This script defines a function `strlen` that calculates the length of a given string. It uses the Python's `len()` function to get the length of the passed string.