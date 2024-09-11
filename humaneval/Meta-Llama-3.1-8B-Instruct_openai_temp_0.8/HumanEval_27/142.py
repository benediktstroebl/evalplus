```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with all characters flipped in case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```

You can use this function like this:

```python
print(flip_case('Hello'))  # Outputs: 'hELLO'
print(flip_case('hELLO'))  # Outputs: 'Hello'
```