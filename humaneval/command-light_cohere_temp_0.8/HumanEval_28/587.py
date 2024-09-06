Here's the self-contained Python script with a function `concatenate` that solves the problem of joining strings:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(''.join(strings) if strings else [''])
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. The function uses the important `List` type hint for the input parameter, which ensures that the expected type of the input is a list of strings.