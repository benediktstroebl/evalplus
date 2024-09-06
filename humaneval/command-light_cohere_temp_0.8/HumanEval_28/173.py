```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join([s + (i == len(strings) - 1 or s)) for i,s in enumerate(strings,1)]
# tests
strings = [''] + ['a', 'bc']
print(concatenate(strings))  # Output: abc
```