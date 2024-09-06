Here's a self-contained Python function that filters an input list of strings based on a given substring: 

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function utilizes the `contains()` method to check if each string in the input list contains the given substring. 

The output list will contain only those strings from the input list that have the substring. 

This solution is concise and self-contained, following the criteria for a good Python function.