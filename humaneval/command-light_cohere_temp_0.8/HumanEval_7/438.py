```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This code defines a function called `filter_by_substring` that takes in a list of strings and a substring as arguments. It then iterates through list elements, and returns a new list containing only the elements that contain the specified substring. The function uses the  the Python in-built function `contains` to check if an element in the list contains the substring.