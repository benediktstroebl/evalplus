```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The code defines a function filter_by_prefix that filters an input list of strings based on a given prefix. It uses the Python's list comprehension to iterate through the input strings and checks if each element starts with the specified prefix. The output is a list of matching strings.