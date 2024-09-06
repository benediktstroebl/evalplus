Here's the self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function leverages the `startswith` method of the string class in Python, which checks if a given string starts with the given prefix. 

It's a concise and efficient way to filter a list based on a given criterion.