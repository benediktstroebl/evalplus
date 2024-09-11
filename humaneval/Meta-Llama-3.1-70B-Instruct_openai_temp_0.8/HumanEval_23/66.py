```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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
    print("All tests passed.")
```

In this code:

- We define the `strlen` function with a docstring that describes what it does and includes usage examples (as per the guidelines in the Python documentation).
- The function itself simply calls the built-in `len` function to get the length of the string.
- We then have a `main` block that includes test cases for the function. These test cases verify that the function behaves as expected.
- If the function passes all the test cases, it prints "All tests passed."