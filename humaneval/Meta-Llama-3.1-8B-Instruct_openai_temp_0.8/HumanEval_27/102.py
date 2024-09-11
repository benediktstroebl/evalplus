### Flipping Case of a String
#### Python Function to Swap Case of Characters

```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Example usage
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case(' WORLD '))  # Output:'wORLD '
```

In this script, we define a function `flip_case` that takes an input string. We use a generator expression to iterate over each character `c` in the string. If `c` is a lowercase character (`c.islower()`), we convert it to uppercase using `c.upper()`. Otherwise, we convert `c` to lowercase using `c.lower()`. The `join` method is then used to concatenate all the characters into a single string.