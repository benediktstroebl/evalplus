```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two arguments: a list of strings (`strings`) and a substring (`substring`). The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, accompanied by an in operator to check for the presence of the substring within each string in the list.  This allows you to filter strings in an efficient and concise manner based on a specific substring.  The function passes the provided tests: filtering empty lists and filtering lists based on the presence of 'a'.