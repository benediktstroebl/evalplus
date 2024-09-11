```markdown
### Flip Case Function

The following Python script defines a function `flip_case` that takes a string as input and returns the string with all lowercase characters flipped to uppercase and all uppercase characters flipped to lowercase.

```python
def flip_case(string: str) -> str:
    """ 
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to be flipped.
    
    Returns:
    str: The string with characters flipped.
    
    Examples:
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

# Example usage
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'HELLO'
```

In this script, the `swapcase` method is used to achieve the desired outcome. This method swaps the case of all characters in the string, effectively flipping the case of all characters.
```