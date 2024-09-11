```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)


# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
```

In this script, the `swapcase()` method is used to change the case of each character in the string. This method converts lowercase characters to uppercase and vice versa. The `join()` method is then used to combine these modified characters back into a single string.