```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that filters a list of strings based on whether their prefix matches a given string prefix. The function uses the string interpolation with the **startswith** method to achieve this. The function returns a list of matching strings.