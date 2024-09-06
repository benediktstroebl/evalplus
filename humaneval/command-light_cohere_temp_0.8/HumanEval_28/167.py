```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate 
    Returns: concatenated string
    """
    assert not strings, "Input list cannot be empty"
    return ''.join(''.join(strings) + '')
```