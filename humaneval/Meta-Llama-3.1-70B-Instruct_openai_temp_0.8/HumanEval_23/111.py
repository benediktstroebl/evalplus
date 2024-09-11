```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3

print("All test cases passed.")
```

This script defines a `strlen` function that calculates the length of a given string using Python's built-in `len` function. The `assert` statements serve as test cases to verify the correctness of the function. If all test cases pass, it prints "All test cases passed."