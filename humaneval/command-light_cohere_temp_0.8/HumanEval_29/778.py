```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It returns al list of strings from the input list that start with the given prefix. 

This function uses a list comprehension to iterate through each string in the input list. 

It uses the `startswith` method, which checks whether a given string starts with a given prefix.