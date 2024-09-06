```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The code defines a function called **`filter_by_substring`** that takes a list of strings and a substring as input. The function uses a search algorithm to return a new list of strings that contain the given substring.