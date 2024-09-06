```python
# Retrieve the requested function
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for string in strings:
        result += string
    return result
```
The code includes a docstring with example usage that outlines the problem and provides test cases. The function iterates through the input list of strings and appends each string to a result string, which is then returned. This solution effectively concatenates the strings, and the descriptive docstring communicates the function's purpose and behavior, aiding users in understanding and implementing the code.