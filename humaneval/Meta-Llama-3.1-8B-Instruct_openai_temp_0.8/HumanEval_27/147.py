```python
def flip_case(string: str) -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    Args:
        string (str): The input string to be flipped.

    Returns:
        str: The input string with all lowercase characters converted to uppercase and vice versa.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
    """
    return ''.join(c.swapcase() for c in string)
```

### Explanation
This function uses a generator expression to iterate over each character `c` in the input `string`. The `swapcase()` method is then called on each character, which flips its case. Finally, the `join()` method is used to concatenate the modified characters back into a string.