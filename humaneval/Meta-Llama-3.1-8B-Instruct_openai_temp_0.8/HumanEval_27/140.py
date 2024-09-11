```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with lowercase characters flipped to uppercase and vice versa.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('Hello World'))  # Output: 'hELLO wORLD'
```

In this script, we define a function `flip_case` that takes a string as input and returns the string with lowercase characters flipped to uppercase and vice versa. The function iterates over each character in the string, checks if it's lowercase using the `islower` method, and appends the corresponding uppercase or lowercase character to the result string. Finally, we test the function with a couple of examples.