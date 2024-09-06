Here is a Python script that includes a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function `filter_by_prefix` filters an input list of strings and returns a new list that includes only the strings that start with the specified prefix. It takes a advantage of the List[str] and List types to create and iterate over the input list.