```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Example usage:
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('hELLO'))  # Output: Hello
print(flip_case('HELLO'))  # Output: hello
```

This script defines a function `flip_case` that uses the built-in string method `swapcase` to flip the case of each character in the input string, and returns the resulting string. The example usage demonstrates the function's behavior with a few test cases.