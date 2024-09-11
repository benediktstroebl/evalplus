```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The input string with flipped case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
if __name__ == "__main__":
    print(flip_case('Hello'))  # Output: 'hELLO'
    print(flip_case('hELLO'))  # Output: 'HELLO'
    print(flip_case('123abc'))  # Output: '123ABC'
    print(flip_case(''))  # Output: ''
```

This script uses a list comprehension to iterate over each character in the string, checking if it's a lowercase character. If it is, it converts the character to uppercase; otherwise, it converts it to lowercase. The `join` method is then used to concatenate the characters back into a string.