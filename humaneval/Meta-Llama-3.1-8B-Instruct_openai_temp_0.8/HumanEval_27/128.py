```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with lowercase characters flipped to uppercase and vice versa.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Outputs: 'hELLO'
print(flip_case('hELLO'))  # Outputs: 'HELLO'
print(flip_case('HeLlO'))  # Outputs: 'hElLo'
```

This Python script defines a function `flip_case` that flips the case of a given string. It uses list comprehension and the built-in string methods `upper`, `lower`, and `islower` to achieve this. The function is then tested with some example inputs.