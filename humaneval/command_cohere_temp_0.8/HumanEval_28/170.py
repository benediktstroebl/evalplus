```python
# Markdown code block
```python
from typing import List

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
The Python script defines a function `concatenate` that takes a list of strings (`List[str]`) as input and returns a single string. The function empties the `result` variable and then iterates through the list of strings, appending each string to the `result` variable. 

The `concatenate` function is designed to accept any list of strings, including an empty list, and return the empty string if the list is empty. The example usage in the function docstring demonstrates this behavior by returning '' for an empty list and 'abc' for a list containing the strings 'a', 'b', and 'c'.  This approach ensures that the function is robust and adaptable to various scenarios.