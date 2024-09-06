```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This function iterates over the input list of strings and returns a new list containing only the strings that contain the given substring. 

This solution is self-contained because it uses the contains() method on string objects, which is part of the Python standard library and does not require any external functions or modules.