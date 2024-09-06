```python
def strlen(string: str) -> int:
    """ Returns length of given string"""
    return len(string)

# Test case 1
assertEqual(strlen(''), 0)
# Test case 2
assertEqual(strlen('abc'), 3)
```
This code defines a function `strlen` which calculates the length of a given string. The function uses the basic Python `len()` function to get the length of the string. The test cases demonstrate the using the `assertEqual` function to check if the length of the output from `strlen` is correct.