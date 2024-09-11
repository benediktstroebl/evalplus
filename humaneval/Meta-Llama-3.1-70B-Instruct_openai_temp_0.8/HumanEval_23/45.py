```python
def strlen(string: str) -> int:
    """
    Return length of given string

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

In this script, the `strlen` function simply uses the built-in `len` function to calculate the length of the input string. The test cases at the bottom ensure that the function behaves correctly for both empty and non-empty strings. If all test cases pass, the script prints "All test cases pass".