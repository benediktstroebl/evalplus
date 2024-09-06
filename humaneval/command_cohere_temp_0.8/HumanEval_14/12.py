```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))));
```
The function `all_prefixes()` uses the `dropwhile()` function from the `itertools` module to iterate over the strings excluding the first element that is equal to an empty string. The resulting list of strings is then reversed to ensure the shortest to longest order and returned to the caller.  This solution has a time complexity of O(n) where n is the length of the input string. It assumes that the string is composed of alphanumeric characters only.