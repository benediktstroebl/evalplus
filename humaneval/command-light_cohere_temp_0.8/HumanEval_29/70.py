```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. The function uses the string slicing and the `startswith` method to return a new list containing only the strings that start with the given prefix. This function demonstrates a good way to filter and transform strings based on a given prefix, allowing for more flexible and efficient string manipulation.