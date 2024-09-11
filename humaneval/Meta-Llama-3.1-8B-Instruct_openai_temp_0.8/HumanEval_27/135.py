```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)


# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('HELLO'))  # Output: 'hELLO'
print(flip_case('hello world'))  # Output: 'HELLO WORLD'
```

This script defines a function `flip_case` which takes a string as input and returns the string with all lowercase characters changed to uppercase and all uppercase characters changed to lowercase. It uses a generator expression to iterate over each character `c` in the input string, applies the `swapcase` method to each character (which swaps its case), and then uses the `join` method to combine the results back into a single string.