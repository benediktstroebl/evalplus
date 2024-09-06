```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function uses the List comprehension to filter the input list of strings based on whether they start with the specified prefix.