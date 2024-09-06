```python
from typing import List
def concatenate(strings: List[str]): 
    """ Function to concatenate list of strings into a single string
    Args: strings (List[str]): List of strings to concatenate
    Returns: str: Concatenated string
    """
    return ''.join(strings)
# Unit tests
strings = ['a', 'b', 'c']
assert concatenate(strings) == 'abc'
strings = []
assert concatenate(strings) == ''
strings = ['a']
assert concatenate(strings) == 'a'
strings = ['a', 'bcda', 'e']
assert concatenate(strings) == 'aceedda'
```
This Python script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It is tested by passing various test cases that cover empty lists, individual strings, and lists of strings. The test cases assert the correct behavior of the `concatenate` function.