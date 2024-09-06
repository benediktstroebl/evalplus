```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This code defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the specified prefix.