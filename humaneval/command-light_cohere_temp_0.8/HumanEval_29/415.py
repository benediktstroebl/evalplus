```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function called **filter_by_prefix** that takes two parameters: a list of strings and a prefix. The function filters the strings in the input list that start with the given prefix. It does this using a function's signature to return a new list containing only the strings from the original list that start with the specified prefix.