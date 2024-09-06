```python
# Retrieve the requested script
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated = ''
    for string in strings:
        concatenated += string
    return concatenated
```

This function takes a list of strings, iterates through them, and appends each string to a concatenated string, which results in a single string. The function is designed to handle an empty list and returns an empty string in such a case. 

The script includes two example tests that align with the problem's prompt, testing the function's ability to handle an empty list and a list with three characters. The output verifies the correct operation of the `concatenate` function. 

To execute the script, simply run it in a Python environment of your choice. It is compatible with Python versions that support type hints and the list comprehension syntax.