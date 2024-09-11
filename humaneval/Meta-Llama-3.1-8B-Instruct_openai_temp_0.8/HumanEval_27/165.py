### Flip Case of a String

Below is a Python function that flips the case of a given string.

```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return string.swapcase()

# Test the function
print(flip_case('Hello'))
print(flip_case('hello'))
```

In this script, we utilize the built-in `swapcase()` method of Python's string class, which swaps the case of each character in the string. This method is more efficient and Pythonic than manually iterating over the characters in the string and swapping their cases.