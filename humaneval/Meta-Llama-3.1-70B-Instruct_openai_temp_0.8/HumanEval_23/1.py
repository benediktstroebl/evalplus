```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


# Test the function
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases pass")
```

This script defines the `strlen` function which takes a string as input and returns its length. It uses Python's built-in `len` function to calculate the length of the string.

The script also includes two test cases at the bottom to verify the correctness of the `strlen` function. If the function is working correctly, it prints "All test cases pass".