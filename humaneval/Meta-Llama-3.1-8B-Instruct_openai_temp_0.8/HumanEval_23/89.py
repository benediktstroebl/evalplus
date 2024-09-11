### String Length Function
#### Problem Description
This script defines a function `strlen` that calculates the length of a given string.

#### Code
```python
def strlen(string: str) -> int:
    """
    Return length of given string

    Args:
        string (str): The input string

    Returns:
        int: The length of the input string

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

#### Explanation
This script uses the built-in `len` function in Python to calculate the length of the input string. The `strlen` function takes a string as input and returns its length as an integer. The docstring provides a description of the function, its arguments, return value, and some examples of usage. The script also includes two test cases to verify the correctness of the function.