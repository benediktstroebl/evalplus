```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
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

However, it's worth noting that Python already has a built-in `len` function for strings, which is more efficient and idiomatic than defining a new `strlen` function. The above code is essentially a wrapper around the `len` function.

Alternatively, if you wanted to manually calculate the length of a string (for educational purposes, perhaps), you could do so with a loop:
```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    length = 0
    for char in string:
        length += 1
    return length

# Test cases
print(strlen('') == 0)
print(strlen('abc') == 3)
```
This version of the function manually iterates over each character in the string and increments a counter, returning the final count as the length.