```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This function uses a list comprehension to filter out any strings from the input list that contain the given substring. 
For example, if you pass the list ['abc', 'bacd', 'cde', 'array'] and the substring 'a', it will return ['abc', 'bacd', 'array'].