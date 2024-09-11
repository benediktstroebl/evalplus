```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.
    
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass")
```

This script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string.

The script also includes two test cases to verify that the function behaves correctly. The `assert` statements will throw an AssertionError if the condition is not met, and the print statement will only execute if all test cases pass.