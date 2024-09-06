```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string in the list.
    Args:
    strings (List[str]): List of strings
    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty or contains strings of different lengths.
    """
    test:
    assert isinstance(strings, List[str]), 'Input must be a list of strings'
    assert not strings or not any(len(s) == len(strings) for s in strings), 'All strings must have the same length'
    return max(strings) if strings else None
```