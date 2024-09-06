```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings
    :return: string
    """
    return ''.join(strings)
# Test cases
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)   # Output: abc
strings = []
result = concatenate(strings)
print(result)   # Output: ''
strings = ['a',''b']
result = concatenate(strings)
print(result)   # Output: ab
strings = ['a', ''.join()b']
result = concatenate(strings)
print(result)   # Output: a....b
```