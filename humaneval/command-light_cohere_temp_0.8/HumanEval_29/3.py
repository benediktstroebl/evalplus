Here is a Python script that includes the function **filter_by_prefix**, which filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function creates an empty list to start, iterates through the input list of strings, and adds an item to the output list if it starts with the given prefix.