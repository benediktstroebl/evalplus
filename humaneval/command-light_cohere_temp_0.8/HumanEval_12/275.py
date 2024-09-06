```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the length of the longest string in the list"""
    longest = str.maketransformer(strings)
    return [len(x) for x in longest]

# Tests
test_longest = [
    assert longest(['a', 'bb', 'ccc']) == 3,
    assert longest([]) == 0,
    assert longest(['aa']) == 1,
]
```
This code defines a function `longest` that takes a list of strings as input and returns the length of the longest string in the list. The function uses a `str.maketransformer` to create a new string from the list of strings, and then uses a list comprehension to find the length of the longest string.