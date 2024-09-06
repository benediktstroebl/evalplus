```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on whether the string contains a given substring. 

The function uses a list comprehension to iterate over the input strings and checks if each string contains the specified substring using the `contains` method.