```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the testing by using the contains() method to check if each string in the list contains the substring.