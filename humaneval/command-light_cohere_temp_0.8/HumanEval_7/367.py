```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This Python function, `filter_by_substring`, takes a list of strings and a substring as inputs. It uses the Using list comprehension with the `find()` method to filter the strings and returns a new list containing only the strings that contain the given substring.