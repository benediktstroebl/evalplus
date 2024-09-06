```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This code defines a function called **`filter_by_prefix`** that takes a list of strings and a prefix as input. It uses the filtering to only include strings that start with the given prefix. The function then returns a list of these matching strings.