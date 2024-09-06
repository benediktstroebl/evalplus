Here's a self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

# Test cases
print(strlen(''))
print(strlen('')) # empty string
print(strlen('abc'))
print(strlen('abc'))
print(strlen('123'))
print(strlen('abc123'))
``` 
This script provides a function `strlen` that accepts a string and returns its length.  It's designed to pass all test cases.