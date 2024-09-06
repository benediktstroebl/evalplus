```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input and returns a new list that contains only the elements that start with the given prefix. The function utilizes the particular characters to determine if a string starts with the given prefix.