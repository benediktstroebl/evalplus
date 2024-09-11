### Case Flipper Script
```python
def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))
print(flip_case('hELLO'))
print(flip_case('HeLlO'))
```

This script defines the `flip_case` function, which takes a string as input and returns a new string with the case flipped. It uses a list comprehension to iterate over each character in the string, converting it to uppercase if it's lowercase and vice versa. The resulting list of characters is then joined back into a string using the `''.join()` method. The script also includes some test cases to demonstrate the function's behavior.