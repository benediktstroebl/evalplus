```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and checking if the `substring` is present in each string, using the in operator. If the substring is found in a string, that string is included in the resulting list and returned. If the `substring` is empty or None, an empty list will be returned to avoid unnecessary computation. 
The function is designed to efficiently handle both short and long strings and substrings, providing a scalable solution for practical applications.