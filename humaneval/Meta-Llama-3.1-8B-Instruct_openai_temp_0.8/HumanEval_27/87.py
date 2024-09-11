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
    return ''.join([char.swapcase() for char in string])

# Test the function
if __name__ == "__main__":
    print(flip_case('Hello'))  # Output: 'hELLO'
    print(flip_case('hELLO'))  # Output: 'Hello'
    print(flip_case('HeLlO'))  # Output: 'hELLO'
```

In this script, the `flip_case` function uses a list comprehension to iterate over each character in the string. The `swapcase()` method is used to flip the case of each character, and these characters are then joined back together into a single string with `''.join()`. 

The script also includes a simple test at the end to demonstrate the function's behavior.