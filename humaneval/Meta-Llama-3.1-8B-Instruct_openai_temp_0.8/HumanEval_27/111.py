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
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Outputs: 'hELLO'
print(flip_case('hELLO'))  # Outputs: 'Hello'
```

This script defines a function `flip_case` that takes a string as input and returns a new string with flipped case. The function uses a generator expression to iterate over each character in the input string, swaps its case using the `swapcase` method, and joins the resulting characters into a single string using the `join` method. The script also includes example usage and test cases to demonstrate the function's behavior.