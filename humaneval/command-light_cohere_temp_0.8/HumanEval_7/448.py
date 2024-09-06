```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function **filter_by_substring** that filters an input list of strings, returning a new list containing only the strings that contain the specified substring. 

The function uses the List comprehension and the contains() method to achieve this. 

Please note that you can use this function with your own input strings and substring as needed.