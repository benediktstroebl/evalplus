```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to be flipped.
    
    Returns:
        str: The string with case flipped.
    
    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)
```

This script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters converted to uppercase and vice versa. The function uses a generator expression within the `join` method to iterate over each character in the string, converting it to uppercase if it's lowercase and vice versa. 

You can test this function with the provided example:

```python
print(flip_case('Hello'))  # Output: 'hELLO'
```