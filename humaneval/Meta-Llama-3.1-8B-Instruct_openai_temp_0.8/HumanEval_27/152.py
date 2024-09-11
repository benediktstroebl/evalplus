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


# Test the function
if __name__ == "__main__":
    print(flip_case('Hello'))  # hELLO
    print(flip_case('hello'))  # HELLO
    print(flip_case('hELLO'))  # hELLO
    print(flip_case('HELLO'))  # hELLO
```

This script defines the `flip_case` function, which uses a generator expression to iterate over each character in the string. If the character is lowercase, it converts it to uppercase; otherwise, it converts it to lowercase. The resulting characters are then joined together into a new string, which is returned by the function. The script also includes some test cases to demonstrate its usage.