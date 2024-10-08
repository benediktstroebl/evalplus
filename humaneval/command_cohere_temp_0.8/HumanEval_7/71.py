```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring` as inputs. It returns a new list containing only the strings from `strings` that contain the specified substring. The function uses a list comprehension, iterating over each string in `strings`, and including it in the new list if it contains the substring.