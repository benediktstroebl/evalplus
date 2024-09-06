```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It returns a a list of strings that start with the specified prefix. The function uses a list comprehension to filter the strings.