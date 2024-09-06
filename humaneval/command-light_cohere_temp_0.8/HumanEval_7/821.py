```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It uses the relevant typing and returns a new list of strings that contain the given substring. 

This function is a good example of a self-contained function, as it can be used directly without relying on any other functions or variables.