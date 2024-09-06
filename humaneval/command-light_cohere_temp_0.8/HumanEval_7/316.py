Here's the solution:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function takes a list of strings and a substring as input and returns a new list that contains only the strings that contain the substring. This is uses the filtering technique, which is common in Python for such list operations.