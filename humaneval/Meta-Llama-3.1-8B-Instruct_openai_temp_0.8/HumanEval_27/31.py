```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([c.swapcase() for c in string])

# Example usage:
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('WORLD'))  # Output: 'wOrLD'
```

In this script, we define the `flip_case` function, which uses a list comprehension to iterate over each character `c` in the input string. The `swapcase()` method is used to flip the case of each character, and the results are joined back together into a single string. The example usage demonstrates the function's behavior with two example inputs.