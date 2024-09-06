```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two arguments: a list of strings (`strings`) and a substring (`substring`). The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, coupled with an in operator to check for the presence of the substring within each string in the list.