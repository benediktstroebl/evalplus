```python
# Retrieve the definition of the function from the above text
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
This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the input strings together. The function includes a docstring that provides a brief description of its purpose, and demonstrates the function's behavior through two example tests that are meant to verify its correctness.  The docstring is not a part of the function but rather provides information to document the functionality for other developers.