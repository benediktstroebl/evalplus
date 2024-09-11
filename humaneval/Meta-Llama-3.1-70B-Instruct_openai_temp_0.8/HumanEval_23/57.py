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
assert strlen('python') == 6

print("All test cases pass")
```