```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings to retain only those that contain a given substring. It uses the method `contains` to iterate over the list of strings and checks if each element contains the provided substring. The output is a list of strings that contain the substring.