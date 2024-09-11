```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return string.swapcase()


# Testing the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hello'))  # Output: HELLO
```

This Python script defines a function called `flip_case` that takes a string as input and returns a new string with lowercase characters converted to uppercase and vice versa. The `swapcase` method of the string class is used to achieve this. The script then includes some example usage of the function.