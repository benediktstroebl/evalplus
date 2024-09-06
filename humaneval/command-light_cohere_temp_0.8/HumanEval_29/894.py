```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix`, which takes a list of strings and a prefix as input. The function returns a filtered list of strings that start with the specified prefix. 

This function uses the list comprehension and the startsswith operator to achieve this. 

The function is designed to be easy to use and understand, and it efficiently filters the input list based on the given prefix.