```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python script defines a function `filter_by_substring` that filters an input list of strings to only include those that contain a given substring. It uses the process similar to iterate through the list of strings and checks if each string contains the given substring using the `find()` method. The filtered list is then returned.