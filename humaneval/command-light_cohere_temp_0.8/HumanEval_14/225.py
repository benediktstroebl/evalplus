```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Returns list of all prefixes from shortest to longest of the input string"""
    return list(itertools.prefixprefixes(string))
```

This code defines a function that uses the itertools.prefix prefix function to generate a list of all prefixes in the given string. It then returns the this list of prefixes.