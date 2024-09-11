```python
def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)
```

### Example Usage:

```python
print(strlen(''))  # Output: 0
print(strlen('hello'))  # Output: 5
printstrlen('world')  # Output: 5
```

### Explanation:

The provided function `strlen` uses Python's built-in `len` function to return the length of the input string. This is a straightforward and efficient solution, as Python's `len` function is implemented in C for performance.