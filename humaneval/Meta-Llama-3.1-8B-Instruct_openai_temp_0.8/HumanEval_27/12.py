### Flip Case Function
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The string with flipped case.

    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
```
This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. It uses a list comprehension to iterate over each character in the string, converting it to uppercase if it's lowercase and vice versa. Finally, it joins the characters back into a string using the `join` method.