```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The code defines a function called **`filter_by_substring`** that takes a list of strings and a substring as input. The function uses the filter method to iterate through the list of strings and returns a new list that contains only the strings that contain the given substring.