```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function called `filter_by_substring` that filters a list of strings based on whether the given substring is present in each string. The function uses the filtering technique by iterating through the input list and checking if each element contains the given substring using the `contains` method. The `contains` method checks if the substring is present in the string, and if it is, the element is included in the filtered list.