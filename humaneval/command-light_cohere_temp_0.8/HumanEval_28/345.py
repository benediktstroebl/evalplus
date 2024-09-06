```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
``` 
This Python code defines a function called `concatenate` that takes a list of strings as an argument and returns a concatenated string. The function utilizes the hangman's technique, combining the strings into a single string, which is then returned. The code is a best practice for handling string concatenation and a good starting point for solving related problems.