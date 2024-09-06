```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 strings = ['abc', 'bacd', 'cde', 'array', 'bad']
    substring = 'a'
    return filter(strings, lambda x: x.find(substring))
```

This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the filtering to create a new list that only contains the strings from the original list that contain the given substring.