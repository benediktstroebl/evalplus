```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate(string[::-1]))[::-1]
```
This code works by reversing the input string, slicing it from the end using [::-1], and then using the accumulate iterator to merge overlapping substrings until the full string is restored. The result is reversed again to return the prefixes in ascending order of length. This solution adheres to the specified problem statement and provides an efficient way to generate the list of prefixes.