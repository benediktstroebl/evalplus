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
print("All test cases passed!")
```
This Python script defines a function `strlen` that calculates the length of a given string and includes test cases to verify its correctness. The `len` function is used to determine the length of the string.