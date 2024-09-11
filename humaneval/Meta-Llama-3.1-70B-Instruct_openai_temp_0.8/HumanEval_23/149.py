```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
assert strlen('') == 0
assert strlen('abc') == 3
print("All test cases pass.")
```

This script defines a function `strlen` that takes a string as an argument and returns its length. The `len` function is used to get the length of the string. The test cases are included in the script to ensure the function works correctly. If all test cases pass, it prints "All test cases pass."