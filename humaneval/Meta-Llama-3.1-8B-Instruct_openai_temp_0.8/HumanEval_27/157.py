```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string to flip case.

    Returns:
    str: The string with case flipped.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
```

In this code:

*   We define a function `flip_case` that takes a string `string` as input.
*   Inside the function, we use a generator expression to iterate over each character `c` in the string.
*   We use `c.islower()` to check if the character is lowercase, and if so, we convert it to uppercase using `c.upper()`.
*   Otherwise, we convert it to lowercase using `c.lower()`.
*   We then use the `join` method to concatenate the converted characters into a single string.
*   Finally, we test the function by printing the result of `flip_case('Hello')`.