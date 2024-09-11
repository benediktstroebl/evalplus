### Flip Case Function
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
    return ''.join(c.swapcase() for c in string)

# Example usage
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
```
This script defines the `flip_case` function which uses the `swapcase()` method to flip the case of each character in the string. The result is then returned as a new string. The example usage demonstrates how to use the function to flip the case of the strings 'Hello' and 'hELLO'.