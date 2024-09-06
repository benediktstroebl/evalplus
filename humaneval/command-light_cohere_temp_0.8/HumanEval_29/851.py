```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on whether their prefixes match a given `prefix`. It uses list comprehension to iterate through each string and checks if its prefix matches the given `prefix` using the `startswith` method. The function returns a string elements that start with the given prefix.