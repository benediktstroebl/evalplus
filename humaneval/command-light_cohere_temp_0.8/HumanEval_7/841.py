```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This script defines a function, `filter_by_substring`, that takes a list of strings and a substring as arguments, and returns a new list of strings that contain the substring. The `contains` method is used to check if each string in the input list contains the given substring. 

This script is self-contained and does not require any additional modules or functions to be defined.