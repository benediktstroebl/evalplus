```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that takes two parameters: a list of strings (`strings`) and a prefix (`prefix`). It uses a list comprehension to iterate over each string in the input list, and if a string starts with the provided prefix, it adds it to the resulting list.