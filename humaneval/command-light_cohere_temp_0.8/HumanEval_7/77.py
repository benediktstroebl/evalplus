Here's the code:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```

This code defines a function `filter_by_substring` that filters an input list of strings to include only those that contain a given substring. The function utilizes the method `find()` of a string to check if the substring exists within the string, and returns the string if the condition is met. 

Note that the `find()` method returns `None` if not found, so we use the conditional check to handle this case.