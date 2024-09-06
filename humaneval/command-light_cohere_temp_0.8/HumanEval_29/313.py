```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that filters a list of strings based on whether their prefix matches a given prefix. The function uses the efficient list comprehension to iterate through the input strings and checks if each element starts with the specified prefix. The output is a list of strings that match the given prefix.