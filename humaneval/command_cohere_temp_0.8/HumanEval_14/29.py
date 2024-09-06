```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function uses the `dropwhile` tool to eliminate prefixes from the start of the string until a prefix is reached where `x != ''`. The list of prefixes is then reversed to ensure the order is correct. As the deepest prefix is reached first during the search, using `dropwhile` and then reversing the list simulates a depth-first traversal of the prefix tree and ensures the shortest prefixes are first.