### String Length Calculator
#### Problem Description
This script defines a function `strlen` that calculates the length of a given string.

#### Code
```python
def strlen(string: str) -> int:
    """
    Return length of given string.

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

# Example usage
if __name__ == "__main__":
    print(strlen(""))  # Output: 0
    print(strlen("abc"))  # Output: 3
```

#### Explanation
The script defines a function `strlen` that takes a string as input and returns its length. The function uses the built-in `len` function in Python to calculate the length of the string. The docstring provides a clear description of the function's purpose, arguments, return values, and examples of usage. The script also includes example usage at the end to demonstrate how to use the `strlen` function.