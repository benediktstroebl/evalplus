```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate
    Returns:
        concatenated string
    """
    return "".join(strings)
# Tests
concatenate([])  # Output: ""
concatenate(['a'])  # Output: 'a'
concatenate(['a', 'b'])  # Output: 'ab'
concatenate(['a', 'bc'])  # Output: 'abc'
concatenate([]) == "" == False  # True
```