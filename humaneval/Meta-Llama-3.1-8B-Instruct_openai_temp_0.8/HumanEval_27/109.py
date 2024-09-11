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
    return string.swapcase()

# Test the function
print(flip_case('Hello'))
print(flip_case('hELLO'))
```

Explanation:
* The `swapcase()` method in Python returns a copy of the string where all uppercase characters have been converted to lowercase and all lowercase characters have been converted to uppercase. This is exactly what the `flip_case()` function needs to do, so we use this method instead of manually swapping the case of each character.