```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function called **`filter_by_prefix`** that filters a list of strings based on a given prefix. The function uses the important list comprehension and a condition to only select strings that start with the specified prefix. This problem effectively filters out all relevant strings and returns a new list with the matched strings.