```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This function uses the `find()` method to check if each string from the input list contains the given `substring`. It returns a new list containing only the strings that have the substring.