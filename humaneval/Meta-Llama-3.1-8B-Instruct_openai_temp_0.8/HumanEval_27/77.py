```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
        string (str): The input string to flip case.

    Returns:
        str: The string with case flipped.

    Example:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])


# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
```

In this script, we define a function `flip_case` that takes a string as input and returns a new string with the case of all characters flipped. We use a list comprehension to iterate over each character in the input string. If the character is lowercase, we convert it to uppercase using `char.upper()`. If the character is uppercase, we convert it to lowercase using `char.lower()`. We join the resulting characters into a single string using the `join()` method. Finally, we test the function with some example inputs.