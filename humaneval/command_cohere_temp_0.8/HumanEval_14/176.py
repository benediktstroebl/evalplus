```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    # Pattern to extract characters from the beginning of the string
    capt = '((.?)(.*?)\2*)'
    # Find all prefixes and pad them to the same length
    prefixes = [re.sub(capt, r'\1\2**\3', string).ljust(len(string), ' ') for _ in range(len(string) + 1)]
    # Remove padding and return sorted list
    return [prefix.rstrip() for prefix in prefixes]
```