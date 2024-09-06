```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function `filter_by_prefix` that filters an input list of strings based on whether each string starts with a specified prefix. The function uses the string comparison to check if each string in the list starts with the given prefix. The output is a list of strings that match the condition. The code is well-contained and demonstrates the problem of filtering strings based on a prefix.