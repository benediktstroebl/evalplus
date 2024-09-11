```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string.

    Returns:
        str: The string with case flipped.
    """
    return ''.join(char.swapcase() for char in string)


# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('aBc'))   # Output: 'ABc'
print(flip_case('123'))   # Output: '123' (no change for non-alphabetic characters)
```

In this script, we use a generator expression within the `join` method to iterate over each character in the input string and apply the `swapcase` method, which flips the case of the character. The resulting string is then returned.