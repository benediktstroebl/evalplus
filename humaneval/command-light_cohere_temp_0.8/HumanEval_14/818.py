```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.list(x) if x != '']
```

This code defines a function called all_prefixes that returns a list of all prefixes of a given string. The function uses the list(string.inter` to create a list of all substrings of the input string, and then it uses a conditional check to filter out any empty characters and keep only the non-empty strings, which are the prefixes of the input string.