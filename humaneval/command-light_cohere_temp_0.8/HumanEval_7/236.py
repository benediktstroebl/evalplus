```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This Python code defines a function called `filter_by_substring`, which filters a list of strings to include only those that contain a given substring. The function uses the for each element in the input list to check if the substring is present, and the result is the list of elements that contain the substring. The type annotations for the string and substring parameters provide better type-checking and enable more detailed comments and better documentation.