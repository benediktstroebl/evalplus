```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. This is a common operation when you need to filter a list of strings based on a certain condition and can be easily performed using list comprehension in Python. 

This approach has a time complexity of `O(n)` since it requires iterating through the input list once and performs a constant time operation ('startswith' call) for each list item.