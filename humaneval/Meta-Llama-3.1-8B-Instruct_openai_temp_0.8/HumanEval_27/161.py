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
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])
```

To test the function, you can run the following code:

```python
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```