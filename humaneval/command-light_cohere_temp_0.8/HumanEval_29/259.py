```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings to return only those that start with a specified prefix. It utilizes the string slicing to achieve this.