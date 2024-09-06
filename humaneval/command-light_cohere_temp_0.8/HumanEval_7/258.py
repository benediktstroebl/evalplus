```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code uses the List comprehension to filter the strings from the `strings` list that contain the `substring` string. 

The containing operation returns a boolean value, and the List comprehension filters out the elements that are not contained in the list.