```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This Python script defines a function **`filter_by_substring`** that filters a list of strings for a given substring. It uses the `find()` method to check if each string in the input list contains the given substring. 

You can use this function to filter and manipulate strings effectively in your Python applications.