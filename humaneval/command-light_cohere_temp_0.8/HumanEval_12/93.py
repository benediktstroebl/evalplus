```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case of empty list.

    # Test case
    a list with only one element
    assert len(strings) == 1, "Input list must contain at least one element."
    # Test a list with multiple equal strings
    assert longest(["a", "bb", "ccc"]) == "ccc", "Returned value does not match expected"
    # Test a list with different lengths
    assert longest(["a", "bc", "ccc"]) == "ccc", "Returned value does not match expected"
    # Test a list containing only empty strings
    assert longest([""]) == None, "Returned value does not match expected"
```