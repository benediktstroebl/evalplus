```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the strings, excluding characters that differ from the prefix (which is an empty string initially). The result is reversed to obtain the prefixes in ascending order. This solution has a time complexity of O(n) where n is the length of the input string, since it involves only one pass through the string.  It returns a list of all prefixes in the input string, from the shortest to the longest.