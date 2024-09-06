```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The above script defines a function called `filter_by_substring` which takes a list of strings and a substring as parameters. It uses the filter action to only include the strings in the list that contain the substring, and the return result is a new list that contains only those strings.