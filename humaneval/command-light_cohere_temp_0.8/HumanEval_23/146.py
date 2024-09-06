Here's a self-contained Python function that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string """
    return len(string)

#Test cases
assertEqual(strlen(''),       0)
assertEqual(strlen('abc')), 3
assertEqual(strlen('abcde')) 
```
This script defines a function strlen that takes a string as an argument and returns its length. The test cases ensure that the function is working correctly for various inputs.