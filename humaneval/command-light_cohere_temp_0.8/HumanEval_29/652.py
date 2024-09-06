Here's the self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function iterates through each string in the input list and checks if the string starts with the specified prefix. It returns a filtered list containing only those strings that match the given prefix.