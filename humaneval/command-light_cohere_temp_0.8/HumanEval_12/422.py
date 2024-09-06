```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the length of the longest string in the list.
    Parameters:
    strings (List[str]): A list of strings.
    Returns: list of the longest string in the list.
    """
    test_
    assert len(strings) != 0, "Input list is empty"
    return max(strings, key=len)
```