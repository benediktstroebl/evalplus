```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    
    Args:
    string (str): The input string to be flipped.

    Returns:
    str: The flipped string.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)


# Test the function
if __name__ == "__main__":
    print(flip_case('Hello'))
    print(flip_case('hELLO'))
    print(flip_case('ALLCAPS'))
    print(flip_case('all lowercase'))
```

In this script, we use a generator expression within the `join` method to swap the case of each character in the string and then join them back together into a single string. The `swapcase` method of a string is used to swap the case of the string's characters.