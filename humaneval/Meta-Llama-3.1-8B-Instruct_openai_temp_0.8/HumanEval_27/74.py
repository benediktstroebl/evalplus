```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(char.swapcase() for char in string)

# Example usage:
print(flip_case('Hello'))  # Output: hELLO
print(flip_case('HELLO'))  # Output: hELLO
```

In this script, the `flip_case` function uses a generator expression to iterate over each character in the input string. The `swapcase()` method is used to flip the case of each character, and the results are joined back into a string using the `''.join()` method.