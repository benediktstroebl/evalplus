### String Length Calculator
#### Python Script

```python
def strlen(string: str) -> int:
    """
    Return length of given string

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

# Test cases
if __name__ == "__main__":
    print(strlen(""))  # Expected: 0
    print(strlen("abc"))  # Expected: 3
```

This script defines a function `strlen` that calculates the length of a given string. It uses the built-in `len` function to achieve this. The function includes a docstring that explains its purpose, input, output, and provides some examples of usage. The script also includes test cases to demonstrate the function's behavior.