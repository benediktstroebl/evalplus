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
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    assert strlen('hello world') == 11
    print("All test cases pass")
```

This script defines the `strlen` function as required and includes test cases to verify that it behaves correctly. The test cases are run when the script is executed directly (not when it's imported as a module). If all test cases pass, it prints a success message. If any test case fails, it raises an `AssertionError`.