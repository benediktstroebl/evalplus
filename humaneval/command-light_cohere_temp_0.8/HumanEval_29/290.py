```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. This is uses the example code that passes the tests and is self-contained, meaning it can be copied and run independently without requiring additional code.