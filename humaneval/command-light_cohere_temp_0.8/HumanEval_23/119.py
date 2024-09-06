Certainly! The code is:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),           0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('')),        0
assertEqual(strlen('     ')), 6
assertEqual(strlen('\\'))    0
assertEqual(strlen(' poorest!')), 11
```
This function can take a string `string` as input and return the length of the given string using the built-in `len()` function.  The sure that way to solve the problem.