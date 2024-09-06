```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x == string[:-1], string[1:]))))
```
The function `all_prefixes()` uses the `dropwhile` function from the `itertools` module to eliminate the entire sequence of characters that match the prefix of the string. It decrements the index progressively until it reaches the end of the string. The resulting sequence is then reversed to ensure the correct order from shortest to longest.