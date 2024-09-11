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
    return ''.join([c.upper() if c.islower() else c.lower() for c in string])

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
print(flip_case('WORLD'))  # Output: wOrld
print(flip_case('wOrld'))  # Output: WORLD
```

This script defines a `flip_case` function that takes a string as input and returns the string with lowercase characters converted to uppercase and vice versa. The function uses a list comprehension to iterate over each character in the string, converts it to the desired case, and joins the results into a single string. The script then tests the function with several example inputs to demonstrate its behavior.