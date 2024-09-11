```python
def flip_case(string: str) -> str:
    """ Flips the case of a given string, turning lowercase characters to uppercase and vice versa.
    
    Args:
    string (str): The input string to be flipped.
    
    Returns:
    str: The flipped string.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))
print(flip_case('hELLO'))
```

This script defines a function `flip_case` that takes a string as input and returns the flipped version of that string. The `swapcase()` method is a built-in string method in Python that swaps the case of all characters in the string. The function uses a generator expression to apply this method to each character in the string, and then joins the result back into a string. The script also includes some test cases to demonstrate the function's behavior.