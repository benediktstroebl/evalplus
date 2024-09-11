```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Args:
    string (str): The input string.

    Returns:
    int: The length of the string.

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('Hello, World!'))  # Expected output: 13
```

Alternatively, if you want to implement the `strlen` function from scratch without using the built-in `len` function, you can do it like this:

```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

    Args:
    string (str): The input string.

    Returns:
    int: The length of the string.

    Examples:
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    length = 0
    for _ in string:
        length += 1
    return length

# Test cases
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
print(strlen('Hello, World!'))  # Expected output: 13
```

Both of these scripts will produce the expected output and pass the provided test cases.