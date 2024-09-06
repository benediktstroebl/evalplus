```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This function uses the contains() method to check if each string in the list contains the given substring. 
The function returns a new list containing only those strings from the input list that contain the substring.