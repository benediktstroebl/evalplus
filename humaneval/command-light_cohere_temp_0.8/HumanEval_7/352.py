```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The `filter_by_substring` function filters an input list of strings to only include those that contain a given substring. It uses the `in List comprehension` to iterate through the input list and checks if each element contains the specified substring.