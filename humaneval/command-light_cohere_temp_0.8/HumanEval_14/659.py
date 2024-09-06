Here is a Python script that contains a self-contained function that returns all prefixes from shortest to longest of an input string.

```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string"""
    return list(sorted(string=str)[:-len(string)//2])
```
This script provides a function all_prefixes that accepts a string and returns a list of its prefixes.  The way it creates this list from the first half of the string, which is the smallest set of characters that forms a prefix.