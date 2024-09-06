```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It uses thef list comprehension to filter the input list and return a new list containing only the strings that start with the given prefix. This function is pure and self-contained and can be used to solve the given problem of filtering strings with a given prefix.