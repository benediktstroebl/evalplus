```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(s) for s in string.
    ]
```
This code defines a function all_prefixes that returns a list of all prefixes of a given string. The list of prefixes is created using list comprehension and the string's characters as the elements.