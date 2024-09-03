```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The code above provides a solution to the problem of filtering an input list of strings for a given substring. 

This function utilizes the `find()` method for each string in the list to check if it contains the specified substring.