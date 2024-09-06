```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This Python code defines a function called `filter_by_substring` that takes two parameters: a list of strings `strings` and a substring `substring`. The function uses a list comprehension to create a new list that contains only the strings from the input list that contain the given substring. This function is generate a test that passes the test and can be used for any list of strings and a substring to filter out the strings that do not contain the substring.