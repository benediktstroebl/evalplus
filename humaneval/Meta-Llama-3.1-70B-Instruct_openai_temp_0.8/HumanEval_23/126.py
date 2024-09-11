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

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

However, if you're trying to implement this function without using Python's built-in `len()` function, you could use a loop to count the characters in the string:

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

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```

Or, using recursion:

```python
def strlen(string: str) -> int:
    """
    Return length of given string
    
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    if string == '':
        return 0
    else:
        return 1 + strlen(string[1:])

# Example usage:
print(strlen(''))  # Output: 0
print(strlen('abc'))  # Output: 3
```