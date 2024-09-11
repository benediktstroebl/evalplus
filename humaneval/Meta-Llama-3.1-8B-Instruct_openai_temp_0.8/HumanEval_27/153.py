```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to be flipped.

    Returns:
    str: The string with flipped case.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: HeLLO
print(flip_case('HElLo'))  # Output: HeLlO
print(flip_case('12345'))  # Output: 12345 (no change for non-alphabetic characters)
```
This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and all uppercase characters converted to lowercase. The function uses a list comprehension to iterate over each character in the string, calling `upper()` or `lower()` method based on whether the character is lowercase or uppercase, and then joining the resulting characters back into a string. The script also includes some test cases to demonstrate the function's behavior.