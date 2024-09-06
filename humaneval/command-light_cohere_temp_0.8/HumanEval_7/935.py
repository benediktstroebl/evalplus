```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 strings: List[str] = ['abc', 'bacd', 'cde', 'array']
    substring: str = 'a'
    return [string for string in strings if string.find(substring) != -None]
```
The problem is to filter an input list of strings only for ones that contain a given substring. We use the filter() function with a lambda function to create a new list that contains only the strings from the original list that contain the given substring.