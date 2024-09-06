```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to iterate over the strings, dropping those that are not the prefix of another string (i.e., dropping the largest prefixes). The resulting list of prefixes is then reversed to ensure the shortest prefixes are first in the list. This is how the function obtains the desired result.