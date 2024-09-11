### String Length Function in Python
Here is a simple self-contained Python script that meets the requirements.

```python
def strlen(string: str) -> int:
    """
    Return the length of a given string.

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

# Test the function
print("Length of empty string:", strlen(""))
print("Length of 'abc':", strlen('abc'))
```

This script defines a function `strlen` that takes a string as input and returns its length. It uses the built-in `len` function to achieve this. The docstring includes a description, argument details, return value details, and examples of how to use the function. The script also includes some test cases to verify the function's correctness.