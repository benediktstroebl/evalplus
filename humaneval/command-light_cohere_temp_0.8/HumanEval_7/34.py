```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This Python script defines a function called `filter_by_substring` that filters a list of strings to only include those that contain a given substring. The function uses the straightforward indexing to iterate over the list of strings, and uses the `find()` method to check if each string contains the given substring.