```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

#Test cases
assertEqual(strlen(''),     0)
assertEqual(strlen(' ')),     0
assertEqual(strlen('abc') , 3)
assertEqual(strlen('abcde')), 4  
```
This code defines a function `strlen` that calculates the length of a given string. It utilizes the simple Python's `len()` function to get the length of the passed string.