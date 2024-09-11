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
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))
```

### How it works:

1. The function `flip_case` takes a string `string` as input.
2. It uses a generator expression to iterate over each character `char` in the string.
3. The `swapcase` method is used to flip the case of each character (converting lowercase to uppercase and vice versa).
4. The `join` method is used to concatenate the flipped characters back into a single string.
5. The function returns the resulting string with flipped case.

This script is a self-contained solution to the problem, including a docstring with example usage and a test case.