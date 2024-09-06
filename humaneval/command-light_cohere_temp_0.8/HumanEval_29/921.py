```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It uses the basic list comprehension to filter the input list, returning a new list that contains only the strings that start with the given prefix. 

This function is self-contained, meaning it can be used to solve the problem without depending on any other functions or variables.