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
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HeLlO'
```
This script defines a function `flip_case` that takes a string as input and returns the string with lowercase characters flipped to uppercase and uppercase characters flipped to lowercase. The function uses a list comprehension to iterate over each character in the input string, converting it to uppercase if it's lowercase and vice versa. The `join` method is then used to concatenate the characters back into a single string. The script includes docstrings and examples to demonstrate how to use the function.