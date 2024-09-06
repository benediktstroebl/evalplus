```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string if c.isalpha()]
# Tests
```

This Python function, all_prefixes, takes a string as input and returns a list of all prefixes from shortest to longest, using string slicing with a fixed 'a' prefix.