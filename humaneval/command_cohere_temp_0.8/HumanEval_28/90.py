```python
# Retrieve the requested function definition and its docstring
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

# Add explicit empty test case
strings = []
result = concatenate(strings)
print('Expected:', '')
print('Got:', result)

# Add explicit test case
strings = ['a', 'b', 'c']
result = concatenate(strings)
print('Expected:', 'abc')
print('Got:', result)
```

This script includes two tests to ensure the function behaves as expected. It verifies that the function handles an empty list as well as a list with three characters. The output is then printed to the console for verification.