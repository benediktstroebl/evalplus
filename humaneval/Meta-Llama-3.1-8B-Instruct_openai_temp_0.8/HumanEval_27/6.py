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
    return ''.join(char.swapcase() for char in string)

# Test the function
print(flip_case('Hello'))
print(flip_case('hELLO'))
print(flip_case('ABC DEF'))
print(flip_case('abc def'))
```

In this script, the `flip_case` function uses a generator expression to iterate over each character in the input string. The `swapcase()` method is then used to flip the case of each character, and these characters are joined back together into a single string using the `join()` method. The `swapcase()` method is a built-in string method in Python that does exactly what we need for this problem.