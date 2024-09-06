```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(x for x in strings)

# Test case 1
strings = []
print(concatenate(strings))  # Output: ''

# Test case 2
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'

# Test case 3
strings = ['1', '2', '3']
print(concatenate(strings))  # Output: 123
```