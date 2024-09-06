```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings to only include those that contain a given substring. The function uses the `contains` to iterate over the input list of strings and checks if each string contains the given substring using the `contains` method. 

This code is self-contained and can be used as a standalone solution to the problem you described.