```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.a:]+[string]
```
This Python function all_prefixes takes a string as input and returns a list of all its prefixes, from shortest to longest, using a generator expression and the alphabet as the source.