```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called **`filter_by_prefix`** that filters an input list of strings based on whether their prefixes match a given target prefix. 

The function uses the list comprehension to iterate through each string in the input list.