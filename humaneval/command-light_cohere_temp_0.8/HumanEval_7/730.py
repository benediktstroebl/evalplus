```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This script defines a function, `filter_by_substring`, that filters an input list of strings to only include those that contain a given substring. 

In this case, the function uses the `find()` method of a string object to check if each string contains the given substring. 

The function returns a new list containing only the strings that meet this condition.