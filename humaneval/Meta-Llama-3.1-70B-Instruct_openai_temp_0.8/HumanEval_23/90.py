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
print("All test cases pass")
```

This script defines a function `strlen` that takes a string as input and returns its length using the built-in `len` function. It also includes two test cases to verify the correctness of the function. If both test cases pass, it prints "All test cases pass".