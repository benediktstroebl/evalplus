```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the length of the longest string in the list """
    longest = str.maketransformer(''.join(strings)
    return [len(x) for x in longest]
```
We use the `str.maketransformer()` to ensure the input is a list of strings, it will be converted to an immutable `List[str]` (Python strings are immutable, so we can't modify the list). The `join_strings` method will return a list of all the concatenated strings in the list.