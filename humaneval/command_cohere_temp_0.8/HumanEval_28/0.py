```python
# Retrieve the requested function definition and its documentation
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
The function `concatenate` takes a list of strings as an argument and returns a single string that concatenates all the inputs. The function is documented with both a summary and an example, which are important for maintaining code readability and understanding. 

This code defines the `concatenate` function and provides a test case for the function. The test case uses the `>>>` prompt to assert the expected behavior of the function.