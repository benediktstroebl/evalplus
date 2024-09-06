```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = []
    num_prefixes = len(re.findall(r"^(.*)\1*", string))
    for i in range(num_prefixes):
        prefixes.append(re.sub(r"^.*\1*", r"\1", string))
    return prefixes
```