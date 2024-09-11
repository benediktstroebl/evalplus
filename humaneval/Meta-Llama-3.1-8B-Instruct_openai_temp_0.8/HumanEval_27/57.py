```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Example usage:
print(flip_case('Hello'))  # Expected output: 'hELLO'
print(flip_case('hello'))  # Expected output: 'HELLO'
```

This script defines a function `flip_case` that takes a string as input and returns a new string with its case flipped. It uses a generator expression to iterate over each character in the input string, swap its case using the `swapcase` method, and then join the resulting characters back into a string. The example usage demonstrates how to use this function with strings containing both lowercase and uppercase characters.