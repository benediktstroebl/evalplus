```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The function `filter_by_substring` filters a list of strings for those that contain a given substring. It uses the search method to find if each element in the list contains the given substring.