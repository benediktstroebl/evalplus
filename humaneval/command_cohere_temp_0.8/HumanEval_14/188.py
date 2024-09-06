```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    # find all non-empty prefixes and sort them alphabetically
    return sorted(re.findall(r'^(\w+)', string), key=len)
```
The code uses `re.findall` to find all non-empty prefixes and then sorts them alphabetically using `sorted`, with the `key=len` argument to sort them by length from shortest to longest.