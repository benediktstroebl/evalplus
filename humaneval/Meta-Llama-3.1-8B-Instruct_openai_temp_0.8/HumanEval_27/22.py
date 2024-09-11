```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The input string with all characters flipped in case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Expected output: 'hELLO'
print(flip_case('hello'))  # Expected output: 'HELLO'
print(flip_case('HeLlO'))  # Expected output: 'hElLo'
```

In this script, the `flip_case` function uses a generator expression to iterate over each character in the input string. The `swapcase()` method is then used to flip the case of each character, before joining them back together into a single string using the `join()` method.