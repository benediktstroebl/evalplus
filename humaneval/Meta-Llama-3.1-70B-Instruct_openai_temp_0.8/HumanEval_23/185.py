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

# Example usage
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

However, if you want to implement it manually (without using the built-in `len()` function), here is an alternative implementation:

```python
def strlen(string: str) -> int:
    """
    Return length of given string

    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    count = 0
    for char in string:
        count += 1
    return count

# Example usage
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```