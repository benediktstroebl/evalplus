```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with lowercase characters converted to uppercase and vice versa.
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('World'))  # Output: 'wORLD'
```

This script uses a list comprehension to iterate over each character in the input string. If the character is lowercase, it converts it to uppercase; otherwise, it converts it to lowercase. The `join` method is then used to concatenate the characters back into a string.