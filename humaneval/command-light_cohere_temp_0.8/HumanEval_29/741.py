```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This script defines a function called **filter_by_prefix** that filters an input list of strings to include only those that start with a specified prefix. 

The function uses the **startswith** method to check if each string in the list starts with the given prefix. 

The function returns a new list containing only those matching strings.