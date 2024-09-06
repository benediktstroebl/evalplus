Certainly! Here's a self-contained Python function that correctly concatenates lists of strings:

```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    >>> concatenate(['a', 'bc'])
    'abc'
    """
    return ''.join(strings)
```
The code defines a function `concatenate` that takes a list of strings as an argument and concatenates them into a single string. The output of the example calls to the function will be the string "abc".

Please use this function to solve the problem and get the expected results.