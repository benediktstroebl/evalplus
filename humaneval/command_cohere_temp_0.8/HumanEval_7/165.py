```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input. It uses a list comprehension to filter the elements of `strings` and return a new list containing only the strings that contain the specified substring. 

This solution passes the given tests and solves the problem in a concise and readable manner.