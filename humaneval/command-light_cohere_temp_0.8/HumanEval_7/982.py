```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
This code defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the approach of using the `find()` function to locate the occurrences of the substring within the input strings.