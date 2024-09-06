```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This script defines a function, `filter_by_substring`, which takes a list of strings and a substring as input, and returns a new list that contains only the strings from the input list that contain the given substring. The function uses the sure the using the `find()` method to check if each string contains the substring, and returns the string if it does.