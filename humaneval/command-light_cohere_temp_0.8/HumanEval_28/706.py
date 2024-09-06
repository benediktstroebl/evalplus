```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(s.join(strings))

# Example usage
strings = ['a', 'b', 'c']
print(concatenate(strings))  # Output: 'abc'
strings = []
print(concatenate(strings))  # Output: ''
```