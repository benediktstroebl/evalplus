Here is a self-contained Python script that solves the problem you described: 
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The function takes a list of strings and a substring as input and returns a new list that contains only the strings from the input list that contain the given substring.