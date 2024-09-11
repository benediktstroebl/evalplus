```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrld'
```

This script defines a function `flip_case` that takes a string as input. It then uses a list comprehension to iterate over each character in the string. If the character is lowercase, it is converted to uppercase; if it is uppercase, it is converted to lowercase. The `join` method is used to combine the modified characters back into a string. The result is then returned by the function. The example usage at the end demonstrates how to use the `flip_case` function with some test cases.