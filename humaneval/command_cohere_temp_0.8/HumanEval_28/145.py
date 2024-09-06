```python
# Retrieve the requested script
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
The `concatenate` function takes a list of strings (`List[str]`) as an argument and returns a single string that concatenates all the strings in the list. It achieves this by iterating through each string in the list and adding it to a running result string. 

The `typing` module is used for type hints, ensuring the function accepts a list of strings and returns a string. Such type annotations are valuable for code clarity and IDE usability.

The included tests verify the function's behavior against empty and non-empty lists, respectively, ensuring the function behaves as expected. In summary, the provided code solves the problem in a concise and well-documented manner.