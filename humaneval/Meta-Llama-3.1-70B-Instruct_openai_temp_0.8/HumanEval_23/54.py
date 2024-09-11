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

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
```

However, a more Pythonic way to write this function would be to simply use the built-in `len` function directly, as it already does exactly what the `strlen` function is supposed to do. So, in practice, you would likely just use `len(string)` instead of defining a custom `strlen` function.

If you want to add some error checking to make sure the input is a string, you could modify the function like this:

```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    return len(string)

# Test the function
print(strlen(''))  # Expected output: 0
print(strlen('abc'))  # Expected output: 3
try:
    print(strlen(123))  # Expected output: TypeError
except TypeError as e:
    print(e)  # Expected output: Input must be a string
```