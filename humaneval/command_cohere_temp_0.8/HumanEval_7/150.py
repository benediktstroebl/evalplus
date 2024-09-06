```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two parameters: a list of strings (`strings`) and a substring (`substring`). The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, where each string in the input list is iterated over, and elements are included in the new list if the substring is found within the string.