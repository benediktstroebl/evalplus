```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string.
    
    Returns:
        str: The string with case flipped.
    
    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([c.swapcase() for c in string])

# Test the function
print(flip_case('Hello'))  # hELLO
print(flip_case('hELLO'))  # HELLO
print(flip_case('hello world'))  # HELLO WORLD
```

This script defines a function `flip_case` that flips the case of each character in the input string. It uses a list comprehension to iterate over each character in the string, calls the `swapcase()` method to flip the case, and then joins the characters back into a string using `''.join()`. The script also includes some test cases to demonstrate the function's behavior.