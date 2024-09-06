Certainly! This script defines a function `strlen` that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Testing the function
>>> strlen('') # This should return 0
#assertEqual(strlen(''), 0)

>>> strlen('abc') # This should return 3
#assertEqual(strlen('abc'), 3)

# Using the function
# print(strlen('hello world')) # Output: 10
```