```python
# The following code is copied verbatim from the manuscript submitted for publication:
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
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
```
This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the input strings together. The function is documented with docstrings that specify its purpose, and provides example usage that demonstrate how to empty list and a non-empty list, respectively. The output of the example usage is included as well to demonstrate the functionality of the function. 
```
This approach provides a clear and concise solution following best practices.