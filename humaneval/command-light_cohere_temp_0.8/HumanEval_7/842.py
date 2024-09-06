```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code implements a function called `filter_by_substring` that filters a list of strings, only keeping those that contain a given substring.  It takes input strings and substring, which are stored in the `strings` and `substring` variables, respectively. The function uses the list comprehension to iterate over each string in the list, and checks whether the string contains the given substring. 

The function returns a new list containing only the strings from the original list that contain the substring.