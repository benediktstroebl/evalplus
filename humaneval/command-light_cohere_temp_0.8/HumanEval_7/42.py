```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This Python script defines a function `filter_by_substring` that filters an input list of strings, returning a new list containing only those strings that contain the given substring. The function utilizes the principle of list comprehension, iterating through the input strings and checking if each element contains the specified substring.