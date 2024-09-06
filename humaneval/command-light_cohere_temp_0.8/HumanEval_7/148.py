```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
The function uses a list comprehension to filter the strings in the input list, based on whether the substring is found within the string.