```python
# Retrieve the requested function definition and its documentation
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    res = ''
    for s in strings:
        res += s
    return res
```

This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the input strings together. The function is documented to specify its purpose and to provide example tests. These examples demonstrate its behavior on two cases: an empty list, and a list with three strings. The documentation is written in markdown format and contains a short description of the function, followed by a code block containing example Python code demonstrating how to use the function.