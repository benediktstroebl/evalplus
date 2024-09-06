```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This Python script defines a function called `filter_by_substring` that filters a list of strings based on whether each element contains a given substring. It utilizes the `find()` method to check for the substring's presence within a string.