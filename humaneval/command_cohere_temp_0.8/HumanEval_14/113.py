```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x == string[0:len(x)], string[1:]+string))))
```

The code uses `dropwhile` to eliminate parts of the string that match substrings of the same length to move through the string from longest to shortest prefix. The resulting list is then reversed to get the order from shortest to longest. This solution has a complexity of O(n) due to the `dropwhile` behaviour.