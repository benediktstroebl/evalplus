```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring` as inputs. It returns a new list containing only the strings from `strings` that contain the specified substring. This is accomplished using a list comprehension, where each string s in `strings` is iterated over, and those that contain the substring substring are included in the new list and returned.  This solution is concise and effectively filters the desired strings from the input list.