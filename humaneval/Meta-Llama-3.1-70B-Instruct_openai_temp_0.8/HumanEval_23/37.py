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

This script defines a function `strlen` that takes a string as input and returns its length. It uses the built-in `len` function in Python to get the length of the string.

The test cases are defined using the `assert` statement, which checks if the condition is true. If the condition is false, it raises an `AssertionError`. The `if __name__ == "__main__":` block ensures that the test cases are run only when the script is executed directly, not when it is imported as a module in another script.