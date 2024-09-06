```python
def strlen(string: str) -> int:
    return len(string)

# Test case for empty string
assertEqual(strlen(''), 0)

# Test case for single character string
assertEqual(strlen('a'), 3)

# Test case for multiple characters string
assertEqual(strlen('abc'), 3)
```
This Python code defines a function `strlen` that calculates the length of a given string. The function uses the Python's built-in `len()` function to get the length of the string. The test cases ensure that the function is working correctly for different inputs.