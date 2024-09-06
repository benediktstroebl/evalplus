```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The filter_by_prefix function filters a list of strings, taking a list of strings and a prefix as input and returning a new list that contains only the strings that start with the given prefix.