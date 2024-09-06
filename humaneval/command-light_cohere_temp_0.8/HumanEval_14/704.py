```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string"""
    return [prefix for prefix in string.range longest_prefix(string) if prefix.startswith(prefix) and len(prefix)>1

def longest_prefix(string: str) -> str:
    """ Returns the longest prefix of the input string"""
    if not string: return ""
    return max((prefix for prefix in string if prefix.startswith(string)), key=len)
```
This code defines a function `all_prefixes` that returns a list of all prefixes from shortest to longest of the input string. The function utilizes the longest_prefix to get the longest prefix and checks if the prefix is a prefix of the string and has a length greater than one, then it is added to the returned list.