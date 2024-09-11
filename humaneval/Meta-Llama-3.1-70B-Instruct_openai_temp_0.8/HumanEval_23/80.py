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
    assert strlen('') == 0
    assert strlen('abc') == 3
    print("All test cases passed.")
```

This script defines a function called `strlen` that uses the built-in Python `len` function to calculate the length of a given string. The script also includes two test cases to verify that the function works correctly. If the function passes both test cases, it prints "All test cases passed."

Note that this function does not handle the case where the input is not a string. If you want to add error checking to handle this case, you could modify the function like this:

```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)


# Test cases
if __name__ == "__main__":
    assert strlen('') == 0
    assert strlen('abc') == 3
    try:
        strlen(123)
    except TypeError as e:
        print(e)  # Input must be a string
    print("All test cases passed.")
```