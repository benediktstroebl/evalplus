```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code defines a function called `filter_by_substring` that takes in two parameters: a list of strings and a substring. The function uses the string method `contains` to check if each string in the list contains the given substring.