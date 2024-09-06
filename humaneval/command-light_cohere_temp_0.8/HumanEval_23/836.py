Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test case 1
assertEqual(strlen(''), 0)

# Test case 2
assertEqual(strlen('abc'), 3)
```
This script defines a function `strlen` that calculates the length of a given string. It uses the `len` to get the length of the provided string, which is the correct way to implement the `len()` function.