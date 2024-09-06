```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This script defines a function called `filter_by_substring` that takes in a list of strings and a substring as arguments. It then iterates through list of strings and returns a new list that contains only the strings that contain the given substring.