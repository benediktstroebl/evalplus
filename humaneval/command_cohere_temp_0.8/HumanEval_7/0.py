```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings that contain the given substring from the given list of strings. It returns a list that includes these filtered strings. The algorithm operates on the principle of generating a new list by iterating through each element in the input list and analyzing whether it contains the specified substring. If it does, the element is added to the new list, and if not, it is excluded.  This provides a convenient and concise solution to the problem, as it furnishes a fresh list comprised of only those strings that contain the provided substring.