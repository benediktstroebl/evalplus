Here's the self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function utilizes the `startswith` method to check if each element in the input list starts with the provided `prefix`. The filtered list will contain the matching strings. 

You can use this function by passing your list of strings and the desired prefix as arguments, and it will return a new list containing only the strings that start with the given prefix.