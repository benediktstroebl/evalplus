Here's the self-contained Python script with a function named `filter_by_prefix`, which filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. The function uses the string `startswith` method to check if a string starts with the given prefix.