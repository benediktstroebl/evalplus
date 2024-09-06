```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    prefixes = [string[:i]+'%' for i in range(len(string)+1)]
    return prefixes
```
This code uses a list comprehension to generate a list of prefixes of the input string. For each position starting from 0 to length of the string, it produces a prefix of the string with an additional character '%' to indicate that it's a prefix.