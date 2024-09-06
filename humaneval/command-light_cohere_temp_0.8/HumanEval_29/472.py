```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The provided Python script defines a function `filter_by_prefix` that filters an input list of strings based on their prefixes. It uses the specific testing to ensure the desired functionality. The function takes two parameters: `List[str]` (input strings) and `prefix: str` (the prefix to search for).