```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    pass
```
This code defines a function called **`all_prefixes`** that takes a string as input and returns a list of its prefixes from shortest to longest. It uses a Python's list comprehension and a generator expression to create all possible prefixes.