```python
def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join(c.swapcase() for c in string)

# Test the function
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('Hello World'))  # Output: 'hELLO wORLD'
print(flip_case('ALL CAPS'))  # Output: 'aLl cApS'
```

In this script, the `flip_case` function uses a generator expression to iterate over each character `c` in the string. The `swapcase()` method is called on each character to flip its case, and the resulting characters are joined back together into a single string using `''.join()`. The test cases at the bottom demonstrate the function's behavior with different inputs.