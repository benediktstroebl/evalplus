```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix` that takes two parameters: a list of strings (`strings`) and a prefix string (`prefix`). The function filters the input list of strings and returns a new list containing only the strings that start with the given prefix. This code demonstrates the0 code provides a concise and effective way to solve the problem of filtering strings based on a given prefix.