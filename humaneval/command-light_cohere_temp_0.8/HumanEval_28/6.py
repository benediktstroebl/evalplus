```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of string
    Returns:
        str: concatenated string
    """
    assert not strings, "Input list cannot be empty"
    return ''.join() + (''.join(strings) if strings else '')
```