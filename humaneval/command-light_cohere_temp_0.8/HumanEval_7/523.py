```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on whether the string contains the given substring using the `find()` method and a generator expression. The `find()` method searches for a specified substring within a string and returns the index if the substring is found.  The function takes a input of a list of strings and a substring and returns a new list of strings that contain the substring, which is the desired output.