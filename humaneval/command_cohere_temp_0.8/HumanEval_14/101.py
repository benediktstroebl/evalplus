```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    # find all non-empty prefixes and sort them by length (ascending)
    prefixes = sorted(re.findall(r'^([^{}]*?)'.format(string), string))
    return prefixes
```