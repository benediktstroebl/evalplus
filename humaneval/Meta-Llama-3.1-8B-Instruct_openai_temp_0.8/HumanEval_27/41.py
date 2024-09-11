### Flip Case Function
```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with flipped case.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Example usage:
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('World'))  # Output: wORLD
print(flip_case('Python'))  # Output: pYTHON
```
In this script, we define the `flip_case` function that takes a string as input and returns the string with flipped case. We use a generator expression with the `join` method to flip the case of each character in the string. The `islower` method checks if a character is lowercase, and the `upper` method converts a lowercase character to uppercase. Similarly, the `upper` method converts an uppercase character to lowercase. Finally, we provide some example usage of the `flip_case` function.