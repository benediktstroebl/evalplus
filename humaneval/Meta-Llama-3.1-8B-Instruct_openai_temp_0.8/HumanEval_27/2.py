```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to flip case.

    Returns:
        str: The input string with case flipped.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)

# Test the function
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
print(flip_case('HeLlO'))  # Output: hElLo
```

In this code:

*   We define a function `flip_case` that takes a string as input and returns the string with case flipped.
*   We use a generator expression within the `join` function to iterate over each character in the input string.
*   For each character, we check if it's a lowercase character using the `islower` method. If it is, we convert it to uppercase using `upper`. If not, we convert it to lowercase using `lower`.
*   We join the modified characters back into a string using `join`.
*   We test the function with some examples to demonstrate its behavior.