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
assert strlen('') == 0
assert strlen('abc') == 3
assert strlen('hello world') == 11
print("All test cases passed.")
```

This script defines a function `strlen` that takes a string as input and returns its length. It uses the built-in `len` function to calculate the length. The script also includes test cases to verify the correctness of the function.