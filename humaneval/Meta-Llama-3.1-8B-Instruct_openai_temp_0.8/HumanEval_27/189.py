```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be flipped.
    
    Returns:
        str: The string with lowercase characters flipped to uppercase and uppercase characters flipped to lowercase.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('World'))  # Output: 'wORld'
print(flip_case('Python'))  # Output: 'pYTHON'
```

In this script, the `flip_case` function uses the `swapcase` string method to flip the case of each character in the input string. The `join` method is then used to concatenate the swapped characters back into a single string. The test cases at the end demonstrate the function's behavior.