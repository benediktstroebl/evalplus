```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
print(strlen('') == 0)
print(strlen('abc') == 3)
```

However, the above code doesn't validate the input. If the input is not a string, it will throw an error. Here is a more robust version:

```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)

# Test cases
print(strlen('') == 0)
print(strlen('abc') == 3)

# Test with invalid input
try:
    print(strlen(123))
except TypeError as e:
    print(e)
```