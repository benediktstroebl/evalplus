Here's the solution that is self-contained and can filter an input list of strings based on their prefixes:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function uses a list comprehension to filter out the strings that start with the given prefix.