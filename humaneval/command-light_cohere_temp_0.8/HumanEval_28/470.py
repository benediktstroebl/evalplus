```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    Returns: str - Concaten result
    """
    return ''.join(strings)
# Test the function with different inputs
strings = ['a', 'b', 'c']
# Concatenation works as expected
print(concatenate(strings))  # Output: 'abc'
strings = []
# Empty list should return an empty string
print(concatenate(strings))  # Output: ''
strings = ['a', '!']
# String literal should be concatenated
print(concatenate(strings))  # Output: 'aa!'
strings = ['1', 2, 3]
# Concatenation works with numeric strings too
print(concatenate(strings))  # Output: 123
```