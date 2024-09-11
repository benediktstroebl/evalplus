### Length of a String in Python
#### Problem Description
This script defines a function `strlen` to calculate the length of a given string in Python.

#### Code
```python
def strlen(string: str) -> int:
    """
    Return length of given string.

    Args:
        string: The input string.

    Returns:
        An integer representing the length of the string.

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

#### Explanation
This script defines a function `strlen` that takes a string as an input and returns its length using the built-in `len` function in Python. The function includes a docstring that describes its purpose, arguments, return values, and provides examples of usage. The script also includes two test cases to demonstrate the function's behavior.