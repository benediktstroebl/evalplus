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
    return ''.join([c.swapcase() for c in string])

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: HELLO
print(flip_case('HElLo'))  # Output: hElLo
```

In this script, we use a list comprehension to iterate over each character `c` in the string, swap its case with `c.swapcase()`, and then join all characters back into a string with `''.join([...])`.