```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function uses the contains method of the string object to check if each string contains the given substring. 

The function returns a new list containing only those strings that contain the substring.