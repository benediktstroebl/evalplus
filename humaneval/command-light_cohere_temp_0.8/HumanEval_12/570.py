```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.
    """
    return max(strings, key=len) if strings else None
    """
    assert longest([]) is None, "Input list is empty"
    assert longest(["a", "bb", "ccc"]) == "ccc", "Wrong output: should be ccc"
    return longest([str for str in "abcdebf"])  # this should be the longest string "debf"
    return None  # this should evaluate to None
```