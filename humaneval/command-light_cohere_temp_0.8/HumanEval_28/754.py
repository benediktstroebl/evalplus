```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Tests
concatenate(['a', 'b', 'c']) # Output: 'abc'
concatenate([])      # Output: ''
concatenate(['aa', 'bb', 'cc']) # Output: 'ccc'
concatenate([1,2,3])  # Output:123
```