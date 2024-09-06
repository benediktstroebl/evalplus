```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It returns a constant time list containing only the strings from the input list that contain the provided substring. This is `contains()` method is used to check if each string contains the substring. 

In summary, this is a well-contained and efficient way of filtering a list of strings for those that contain a given substring.