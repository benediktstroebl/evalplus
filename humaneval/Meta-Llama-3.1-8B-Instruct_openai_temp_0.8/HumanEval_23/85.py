### String Length Calculator
#### Python Script

```python
def strlen(string: str) -> int:
    """
    Return length of given string

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

# Test the function
print(strlen(""))  # Output: 0
print(strlen("abc"))  # Output: 3
```

In this script, we define a function `strlen` that takes a string as input and returns its length using the built-in `len` function. The function also includes a docstring that describes its purpose, arguments, and return values, as well as some examples of its usage. The script then tests the function with two example inputs: an empty string and a string with three characters.