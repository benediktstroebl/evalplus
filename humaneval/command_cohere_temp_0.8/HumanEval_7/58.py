```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `List[str]`, containing only the strings from the input list that contain the given substring. It uses a list comprehension, creating a new list, and the in operator to check if the substring is present in each string in the input list. 

This solution has a time complexity of `O(n)` since it requires iterating through the input list once to check for the presence of the substring in each string, where `n` is the length of the input list.