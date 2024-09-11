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


# Example use cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

This script defines a function `strlen` that takes a string as an input and returns its length. The function uses Python's built-in `len` function to calculate the length of the string.

The example use cases demonstrate how to use the `strlen` function. The `assert` statements verify that the function behaves as expected, and the `print` statement indicates that all test cases pass.

You can run this script directly to test the `strlen` function.