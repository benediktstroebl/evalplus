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
print(strlen('') == 0)  # Should print: True
print(strlen('abc') == 3)  # Should print: True
```