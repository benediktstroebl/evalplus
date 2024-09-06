```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the time complexity of O(n), where n is the length of the input strings list, since it simply iterates over the list.