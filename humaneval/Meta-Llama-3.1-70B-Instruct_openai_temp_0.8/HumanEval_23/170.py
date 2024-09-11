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
    assert strlen('') == 0, "Test case failed: strlen(\'\') should return 0"
    assert strlen('abc') == 3, "Test case failed: strlen(\'abc\') should return 3"
    print("All test cases pass")
```

In this script, the `strlen` function simply uses the built-in Python `len` function to return the length of the given string. The test cases are included at the end to verify that the function behaves as expected.