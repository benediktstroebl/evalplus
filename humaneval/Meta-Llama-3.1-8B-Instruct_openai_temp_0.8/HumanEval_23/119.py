### Length of a String in Python
#### Problem Description
The following Python script defines a function `strlen` that calculates the length of a given string.

```python
def strlen(string: str) -> int:
    """
    Return the length of the given string.

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
if __name__ == "__main__":
    print(strlen(""))  # Output: 0
    print(strlen("abc"))  # Output: 3
```

This script uses Python's built-in `len` function to calculate the length of the input string. The function takes a string as input and returns an integer representing the string's length. The docstring provides a clear description of the function, its arguments, and its return value, along with examples of usage. The test cases in the `if __name__ == "__main__":` block demonstrate the function's behavior for an empty string and a non-empty string.