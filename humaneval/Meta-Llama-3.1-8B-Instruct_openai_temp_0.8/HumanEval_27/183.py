```python
def flip_case(string: str) -> str:
    """
    Flips the case of all characters in a given string.

    Args:
        string (str): The input string.

    Returns:
        str: The string with all characters flipped in case.
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('hELLO'))  # Output: 'Hello'
print(flip_case('HeLlO'))  # Output: 'hElLo'
```

This script uses a generator expression to iterate over each character in the input string. If the character is lowercase (`c.islower()` returns `True`), it converts it to uppercase with `c.upper()`. Otherwise, it converts it to lowercase with `c.lower()`. The `join()` method then combines these characters back into a single string, which is returned by the `flip_case()` function.