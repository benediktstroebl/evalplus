The solution is a Python script with a self-contained function that filters an input list of strings based on a given prefix.

```python
from typing import List

# Function to filter strings with a given prefix
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the `startswith` method to check if each string in the input list starts with the given prefix. It then returns a filtered list of strings.