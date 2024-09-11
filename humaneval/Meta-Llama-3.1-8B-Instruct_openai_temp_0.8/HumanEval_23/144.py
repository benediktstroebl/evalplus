```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Example:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)


# Test cases
print(strlen(""))  # Expected output: 0
print(strlen("abc"))  # Expected output: 3
```

However, the original function name `strlen` is similar to the name of a standard C function to calculate the length of a string. Pythonic way is to follow PEP 8 which suggests that function names should be lowercase, with words separated by underscores as necessary to improve readability. Therefore, it would be better to rename the function to `calculate_string_length`. Here's the modified version:

```python
def calculate_string_length(string: str) -> int:
    """
    Return length of given string.

    Args:
        string (str): The input string.

    Returns:
        int: The length of the input string.

    Example:
        >>> calculate_string_length('')
        0
        >>> calculate_string_length('abc')
        3
    """
    return len(string)


# Test cases
print(calculate_string_length(""))  # Expected output: 0
print(calculate_string_length("abc"))  # Expected output: 3
```