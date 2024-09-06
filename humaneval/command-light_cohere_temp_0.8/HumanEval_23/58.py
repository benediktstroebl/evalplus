Here is a Python script with a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
assertEqual(strlen(''), 0)

# Test case 2
assertEqual(strlen('abc'), 3)
```
The `strlen` function takes a string as input and returns the length of the string using the built-in `len()` function. It passes the through test cases with the `assertEqual` function, which checks if two expressions are equal and will raise an AssertError if they are not.