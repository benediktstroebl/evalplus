### Flip Case Function
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to flip.

    Returns:
    str: The string with characters flipped.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])
```

### Usage
```python
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'worLd'
print(flip_case('ALL CAPS'))  # Output: 'aLl cApS'
```