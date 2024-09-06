```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This function takes two arguments: a list of strings and a substring. It then uses a filtering technique to create a new list that contains only the elements of the original list that contain the given substring.