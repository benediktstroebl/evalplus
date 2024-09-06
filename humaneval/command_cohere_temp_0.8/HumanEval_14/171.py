```python
from typing import List
from itertools import dropwhile


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return list(reversed(list(dropwhile(lambda x: x != '', string))))}
```
This code uses the dropwhile function from the itertools module to generate a list of all prefixes of the input string, based on the specified specification. The list comprehension then filters out the empty string that the dropwhile function would initially produce, resulting in a list of prefixes in the desired order.