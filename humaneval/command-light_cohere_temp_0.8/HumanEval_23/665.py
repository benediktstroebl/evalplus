Here is a self-contained Python script that defines a function strlen that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test the function
>>> strlen('') # Output: 0
>>> strlen('abc') # Output: 3
>>> strlen('') == 0  # Output: True
>>> strlen('abc de') == 6 # Output: True
```

This script provides a function `strlen` that calculates the length of a given string, and passes all the tests.