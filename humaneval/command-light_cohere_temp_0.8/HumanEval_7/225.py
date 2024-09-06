```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings to include only those that contain a given substring. It utilizes the `find()` method to locate the substring within each string.