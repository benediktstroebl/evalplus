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
    print("All test cases pass.")
```

This script defines a function `strlen` that takes a string as input and returns its length. It uses Python's built-in `len` function to compute the length of the string.

The script also includes two test cases at the end to verify that the function works correctly. If all test cases pass, it prints "All test cases pass." to the console.