```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This function, `filter_by_prefix`, takes a list of strings and a prefix as arguments. It uses the process similar to filter the input strings and returns a new list that contains only the strings that start with the given prefix.