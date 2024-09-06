```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python code defines a function `filter_by_substring` that filters an input list of strings and returns a new list that includes only the elements that contain a given substring. The function uses the filtering technique by iterating through the input list and checking if each element contains the specified substring using the `contains` method.