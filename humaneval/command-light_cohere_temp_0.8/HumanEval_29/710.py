Here's the Python script with the self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the specified prefix. It uses the string.startswith to check if a string starts with the given prefix.