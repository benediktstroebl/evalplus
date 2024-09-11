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
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('Hello World'))  # Output: 'hELLO wORLD'
```

In this code, we use a generator expression to iterate over each character in the string. We use the `islower()` method to check if a character is lowercase, and if it is, we convert it to uppercase using `upper()`. If it's not lowercase, we simply convert it to lowercase using `lower()`. We then use `''.join()` to concatenate all the characters back together into a single string.