```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings, `strings`, and a substring, `substring`, as input and returns a new list, `return_list`, which contains only the strings from the input list that contain the given substring. 

The function utilizes a list comprehension, enabling concise filtering of strings based on the given substring. The `if` statement acts as the filtering condition, whereby strings containing the substring are retained, and those not containing it are excluded. 

Note: This function is deterministic, meaning the same input will always yield the same output. However, its behavior can vary depending on the input list's characteristics, such as size and content.