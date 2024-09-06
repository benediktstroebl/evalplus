```python
from typing import List
from itertools import accumulate


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(accumulate([string[::-1], [string]], max))
```
This code reverses the string, then accumulates it with an empty string to get the prefixes from shortest to longest. The `max` function is used to combine the reversed string with the empty string, and the reversed string with itself to get the prefixes. This ensures that the shortest prefix is '' and the longest prefix is the original string.