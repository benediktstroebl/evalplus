```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python function uses the startswith() string method to check if each string in a list begins with the provided prefix. The function then returns a list containing only the strings that match this condition.