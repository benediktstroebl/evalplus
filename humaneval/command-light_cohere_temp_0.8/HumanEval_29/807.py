```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This code defines a function called **`filter_by_prefix`** that takes a list of strings and a prefix as input. It uses the`List list comprehension` to filter the input list, only keeping the elements that start with the specified prefix.