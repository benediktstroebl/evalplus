```python
def flip_case(string: str) -> str:
    """
    Flips the case of a given string, converting lowercase to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The input string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)


# Example usage:
if __name__ == "__main__":
    print(flip_case('Hello'))  # Output: 'hELLO'
    print(flip_case('hELLO'))  # Output: 'Hello'
```

This script defines a function `flip_case` that takes a string as input and returns the string with its case flipped. It uses a generator expression to iterate over each character in the string, converting it to lowercase if it was originally uppercase and vice versa. The result is then joined back into a string and returned. The example usage at the end demonstrates how to use the function.