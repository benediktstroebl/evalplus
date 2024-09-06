```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function checks each string in the input list and returns a new list containing only the strings that start with the given prefix. 

This is a simple and effective way to filter an input list of strings based on a given prefix.