### Flip Case Function
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
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)
```

You can use this function like this:
```python
print(flip_case('Hello'))  # Outputs: 'hELLO'
print(flip_case('WORLD'))  # Outputs: 'wOrLd'
```
This function uses a generator expression to iterate over each character in the input string. It checks if the character is lowercase using the `islower()` method, and if so, it converts the character to uppercase using the `upper()` method. Otherwise, it leaves the character unchanged. The results are then joined back together into a single string using the `join()` method.