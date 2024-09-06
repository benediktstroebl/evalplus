```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    prefixes = [string[:i]+('' if i==0 else '') for i in range(len(string)+1)]
    return prefixes
```

The function `all_prefixes` takes a string and returns a list of all prefixes of this string in Python. The list is ordered from the shortest prefix, which is an empty string, to the longest one. The function uses a list comprehension with `range(len(string)+1)` which generates numbers from 0 to length of the string. These numbers are used to slice the string and create all the possible prefixes. The empty string is added to the prefix whenever it's not the 0th index to denote the non-empty prefixes.