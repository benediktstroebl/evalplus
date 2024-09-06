Here is a self-contained Python script that implements the filter_by_prefix function and passes all the tests:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list that contains only the strings that start with the specified prefix. It uses the ** `startswith` method to filter the strings by their prefix.