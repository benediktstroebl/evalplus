```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This code implements a function called **filter_by_substring** that takes in a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. 
It uses the Python's **contains** method to check if each string in the input list contains the given substring.