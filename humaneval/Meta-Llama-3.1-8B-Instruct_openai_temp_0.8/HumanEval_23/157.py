```python
# Function to calculate the length of a given string
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the string

    Example:
        >>> strlen('')
        0
        >>> strlen('abc')
        3
    """
    # Use built-in len() function to calculate the length of the string
    return len(string)

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

This script defines a function `strlen` that calculates the length of a given string using the built-in `len()` function. The function includes a docstring that explains its purpose, arguments, and return value, as well as provides example usage. The script then tests the function with the provided examples.