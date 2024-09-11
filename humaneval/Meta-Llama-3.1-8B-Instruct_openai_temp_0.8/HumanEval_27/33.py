```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
    string (str): The input string.

    Returns:
    str: The modified string with case flipped.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))
```

In this script:

1.  We define a function called `flip_case` that takes a string as an input and returns the modified string.
2.  We use a generator expression inside the `join` function to iterate over each character in the string.
3.  For each character, we check if it's lowercase using the `islower` method. If it is, we convert it to uppercase using the `upper` method; otherwise, we convert it to lowercase using the `lower` method.
4.  We join the characters back into a string and return the result.
5.  We provide a docstring that explains the function's purpose, parameters, and return value, as well as an example usage.
6.  Finally, we test the function with the example input `'Hello'` and print the result.