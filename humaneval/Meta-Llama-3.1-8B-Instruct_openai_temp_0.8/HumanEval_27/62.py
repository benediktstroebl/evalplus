```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with lowercase characters flipped to uppercase and uppercase characters flipped to lowercase.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.swapcase() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hello'))  # Output: HELLO
```

This script defines the `flip_case` function, which takes a string as input, iterates over each character, swaps the case of the character using the `swapcase` method, and then joins the characters back into a string. The function is then tested with two examples to demonstrate its usage.