```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Example usage
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('Hello World'))  # Output: hELlO wOrLd
```

This script defines a function `flip_case` that uses a generator expression to iterate over each character in the input string, swap its case using the `swapcase` method, and join the resulting characters back into a string. The example usage demonstrates how to use this function to flip the case of different strings.