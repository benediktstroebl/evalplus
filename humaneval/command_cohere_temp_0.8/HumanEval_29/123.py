```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate through each string in the input list and check if it starts with the provided prefix using the `startswith` method. If a string starts with the prefix, it's included in the resulting list. If it doesn't, it's not included in the list. 

This solution passes the given tests because:
```
- If the input list is empty, the function returns an empty list.
- If the input list contains 'abc', 'bcd', 'cde', 'array', and the prefix is 'a', the function returns ['abc', 'array'].
```