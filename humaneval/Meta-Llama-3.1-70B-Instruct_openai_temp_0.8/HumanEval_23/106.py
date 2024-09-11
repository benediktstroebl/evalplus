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
    assert strlen('') == 0, f"Expected strlen('') to return 0, but got {strlen('')}"
    assert strlen('abc') == 3, f"Expected strlen('abc') to return 3, but got {strlen('abc')}"
    print("All test cases passed.")
```

This Python script defines a function `strlen` that returns the length of a given string. The `len` function is a built-in Python function that returns the number of items in an object. When the object is a string, it returns the number of characters in the string.

The script also includes two test cases at the end. These test cases ensure that the `strlen` function behaves correctly for an empty string and a string containing three characters. If the function behaves as expected, it prints "All test cases passed."