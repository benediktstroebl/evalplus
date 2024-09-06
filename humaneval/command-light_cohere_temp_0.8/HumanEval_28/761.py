```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate
    Returns:
    str: Concatenated string
    """
    return "".join(strings)
# Tests
concatenate([])  # Output: ''
concatenate(['a'])  # Output: 'a'
concatenate(['a', 'bc'])  # Output: 'abc'
concatenate([123])  # Raises ValueError: cannot concatenate str with str
concatenate(['aa', 'bc']) # Raises ValueError: too many items to concatenate
```