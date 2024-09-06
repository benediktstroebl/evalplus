```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `List[str]`, containing only the strings from the input list that contain the specified substring. It uses a list comprehension, creating a new list, and the in operator to check if the substring is present in each string of the input list. 

This solution has a complexity of O(n^2) due to the use of the in operator, which has a time complexity of O(n) for each string in the list, but it only needs to check the presence of the substring once for each string, so the total complexity is O(n), the number of strings in the list.