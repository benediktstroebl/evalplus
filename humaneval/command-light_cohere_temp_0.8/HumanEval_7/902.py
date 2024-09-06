```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.contains(substring)]
 filter_by_substring([], 'a')  # []
filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')  # ['abc', 'bacd', 'array']
```
The code defines a function **filter_by_substring** that filters a list of strings based on whether the substring is present in each string. This function uses theread list of strings and a given substring, it returns a new list that contains only the strings that contain the given substring.