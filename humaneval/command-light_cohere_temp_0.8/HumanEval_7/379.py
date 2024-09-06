```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function uses the contains() method to check if each string in the input list contains the given substring. 
It returns a list of all the strings from the list that contain the substring.