```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The code defines a function called **filter_by_substring** that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. 
The code uses the Python's **contains** method to check if each string in the input list contains the given substring.