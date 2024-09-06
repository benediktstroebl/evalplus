```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. 

The function uses the `startswith` method from the string module to filter the strings in the list based on whether they start with the given prefix.