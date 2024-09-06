Here is a Python script that contains a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function employs the `startswith` method of string in Python to identify if a given string begins with the provided prefix. The output is a list containing only those strings from the input list that match the specified prefix.