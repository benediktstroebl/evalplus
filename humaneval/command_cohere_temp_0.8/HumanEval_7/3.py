```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This solution makes use of list comprehension, and the python `in` operator to filter strings efficiently. 

For example, if we have the input `['abc', 'bacd', 'cde', 'array']` and the substring `'a'`, the function would return `['abc', 'bacd', 'array']`. 

This approach has a time complexity of `O(n)` since it requires iterating through the list of strings only once, and the built-in `in` operator has a time complexity of `O(n)` as well.