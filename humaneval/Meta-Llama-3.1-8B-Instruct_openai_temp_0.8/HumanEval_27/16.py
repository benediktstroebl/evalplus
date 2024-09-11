Here's a Python script that defines a function to flip case for a given string:
```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to flip the case for.

    Returns:
        str: The string with flipped case.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
print(flip_case('aBcDe'))  # Output: aBcDe
```
In this script, the `swapcase()` method of the string class is used to swap the case of each character in the string, which is achieved by using a list comprehension with `join()` to create the resulting string.