```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.codes string if prefix not '']
```

This code defines a function all_prefixes that takes a string as input and returns a list of all prefixes in the string, excluding the empty string itself.  The process uses list comprehension with a generator expression to achieve this. 

This code is self-contained and does not require any external modules or functions.