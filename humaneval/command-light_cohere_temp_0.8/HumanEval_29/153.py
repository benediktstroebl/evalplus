Here is a self-contained Python script that includes a function `filter_by_prefix`, which is designed to solve the problem you've described:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function utilizes the `startswith` method to filter the strings in the input list, resulting in a new list containing only the strings that start with the specified prefix.