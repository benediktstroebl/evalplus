```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input. The function uses a list comprehension with the **startswith** method to filter out only the elements that start with the given prefix.