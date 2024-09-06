```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The code snippet defines a function called **`filter_by_substring`** that takes in a list of strings and a substring as input. It uses the  the filtering technique to return a new list that contains only the strings from the input list that contain the given substring.