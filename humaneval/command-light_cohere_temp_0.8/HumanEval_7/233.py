```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This script defines a function `filter_by_substring` that filters an input list of strings, returning a new list that includes only the strings that contain a given substring. 

The `contains` statement correctly passes the `List[str]` and `str` types, and the `contains` statement correctly passes the `List` and `substring` as arguments to the `filter_by_substring` function. 
 The output would be a list of strings that contain the given substring.