```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two arguments: a list of strings called `strings` and a substring referred to as `substring`. The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, where each string in the input list is checked to see if the given substring is a part of it. If it is, the string is added to the resulting list. 

The function's description and example usage are also provided to explain its purpose and how it can be used.