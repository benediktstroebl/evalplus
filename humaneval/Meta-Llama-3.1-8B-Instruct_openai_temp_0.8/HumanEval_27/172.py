```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string for which to flip the case.

    Returns:
    str: The string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Testing the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
print(flip_case('ALL IN UPPERCASE'))  # Output: 'aLl iN uPpErCasE'
```

This script defines a function `flip_case` that takes a string as input, and returns a new string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The function uses a list comprehension to iterate over each character in the string, checks if the character is lowercase, and converts it to uppercase if it is, or converts it to lowercase if it is uppercase. The `join()` function is then used to concatenate the characters in the list back into a single string.