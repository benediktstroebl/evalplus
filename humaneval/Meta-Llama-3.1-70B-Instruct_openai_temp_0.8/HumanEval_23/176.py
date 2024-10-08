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
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases passed.")
```

This script defines a function `strlen` that takes a string as input and returns its length. It uses Python's built-in `len` function to calculate the length of the string.

The test cases at the end of the script check that the function works correctly for an empty string and a string with multiple characters. If both test cases pass, it prints "All test cases passed."