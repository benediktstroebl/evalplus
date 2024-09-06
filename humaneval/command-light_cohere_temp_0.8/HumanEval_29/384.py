```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]
```

The above function takes a list of strings and a prefix as parameters. It then iterates through the general strings and filters out the ones that do not start with the given prefix.