```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(''.join(strings, sep='')
```
This function takes a list of strings as input and concatenates them into a single string, with an empty string as the separator between the strings. It is using the string.