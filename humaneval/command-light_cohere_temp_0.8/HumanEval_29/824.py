```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function **`filter_by_prefix`** that filters an input list of strings based on their prefix. It utilizes the string starting method **`startswith`** to iterate through the input strings and returns a new list containing only the strings that start with the specified prefix. 

The function is self-contained and can be used to solve the problem of filtering strings based on their prefixes.