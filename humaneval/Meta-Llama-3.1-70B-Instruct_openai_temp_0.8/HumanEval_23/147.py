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
assert strlen('') == 0, "Test case 1 failed"
assert strlen('abc') == 3, "Test case 2 failed"

print("All test cases passed.")
```

This script defines a function `strlen` that takes a string as input and returns its length. It uses the built-in `len` function to calculate the length of the string. The test cases are run using Python's `assert` statement to ensure the function behaves as expected. If all test cases pass, it prints "All test cases passed."