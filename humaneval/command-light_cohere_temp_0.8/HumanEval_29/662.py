Here is a Python script that contains a self-contained function that filters an input list of strings based on a prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function utilizes the `startswith` method to efficiently filter the input strings. The output is a list of strings that start with the specified prefix.