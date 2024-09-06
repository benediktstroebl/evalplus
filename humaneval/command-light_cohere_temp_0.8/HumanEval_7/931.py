```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The script defines a function called `filter_by_substring` that takes in a list of strings and a substring as input. The function uses a string method `find` to check if each string contains the given substring. This returns a all list of strings that contain the given substring.