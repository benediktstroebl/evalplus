```python
def strlen(string: str) -> int:
    """Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

    Examples:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    return len(string)
```

You can also use the `len()` function directly without defining a separate function. However, in this example, we're defining a function for clarity and to match the expected behavior.

```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```