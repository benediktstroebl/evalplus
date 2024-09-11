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
    assert strlen('hello world') == 11
    print("All test cases passed.")
```

This Python script defines the `strlen` function that returns the length of a given string using the built-in `len` function. It includes test cases at the end to verify the correctness of the function. The test cases are executed when the script is run directly (not when it's imported as a module in another script).