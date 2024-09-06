Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1:
assertEqual(strlen(''), 0)

# Test case 2:
assertEqual(strlen('abc'), 3)

# Test case 3:
assertEqual(strlen('abcde'), 6)
```
This script provides a function `strlen` that calculates the length of a given string. The function uses the method `len` which returns the length of the passed string. The test cases ensure the test that the function works correctly with different inputs.