```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function called **filter_by_prefix** that filters an input list of strings, passing those that start with a specified prefix. 
It uses the list comprehension to create a new list containing only the elements from the original list that start with the specified prefix.