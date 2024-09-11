```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([c.swapcase() for c in string])

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines a function `flip_case` which takes a string as input and returns the string with its case flipped. The function uses a list comprehension to iterate over each character in the string, swap its case with `c.swapcase()`, and then joins the characters back into a string with `join()`. The test cases demonstrate the function's behavior on two sample inputs, 'Hello' and 'hELLO'.