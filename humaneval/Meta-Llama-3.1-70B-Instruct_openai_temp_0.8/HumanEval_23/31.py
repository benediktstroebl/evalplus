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
    print("All test cases pass")
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function in Python. The `if __name__ == "__main__":` block contains test cases to verify that the function behaves correctly.