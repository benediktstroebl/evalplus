```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code defines a function called **filter_by_substring** that filters an input list of strings and returns a new list that contains only the elements that contain a given substring. The function uses the **List[str]** as the input type for both the strings and substring parameters, and it uses the **find()** method from the strings list to filter the strings that contain the substring.