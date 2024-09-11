```python
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

However, this can be further simplified by simply using the built-in `len` function in Python. Here's a revised version of the script:

```python
# Since Python has a built-in len() function, we don't actually need to define strlen()
print(len(''))  # Expected output: 0
print(len('abc'))  # Expected output: 3
```