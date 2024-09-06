Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that takes a list of strings and a prefix as input. The function uses the string method **startswith** to filter and return only the strings that start with the given prefix.