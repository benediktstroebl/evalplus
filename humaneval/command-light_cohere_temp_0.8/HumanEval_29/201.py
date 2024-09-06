Here is a self-contained Python script that defines a function filter_by_prefix that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function filter_by_prefix that takes a list of strings and a prefix parameter, and returns a new list that contains only the strings from the input list that start with the given prefix. 

Please note that this code is a fully functional implementation, and it does not rely on external libraries or modules.