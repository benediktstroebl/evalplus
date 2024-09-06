```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The function filter_by_substring takes a list of strings and a substring as input and returns a new list of strings that contain the substring. 

This function uses a list comprehension to iterate through the input list of strings, and for each string, it checks if the string contains the given substring using the contains() method.