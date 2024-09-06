Here's the solution:

```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This script defines a function called `filter_by_substring` that filters a list of strings and returns a new list that contains only the strings that contain the given substring. 

This function utilizes the typing module to ensure that the input parameters have the correct types, and it uses the contains() method to check if each string in the input list contains the given substring.