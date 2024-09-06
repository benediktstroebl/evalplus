```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python function uses the starts-with operator to filter a list of strings, returning only the ones that start with a specific prefix. It takes in a list of strings and a prefix string as input, and passes corresponding tests.