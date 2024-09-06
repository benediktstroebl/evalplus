```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function utilizes the starts-with operator to filter a list of strings and only retain those that start with the specified prefix. It is a complete self-contained function that can be used as a stand-alone solution to the given problem.