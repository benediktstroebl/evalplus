```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This function uses the contains() method to check if each string in the input list contains the given substring.  It uses list comprehension to filter out the desired strings.