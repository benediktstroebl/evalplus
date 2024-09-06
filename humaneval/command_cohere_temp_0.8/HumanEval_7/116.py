```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings (`strings`) and a substring (`substring`) as input and returns a new list of strings that contain the specified substring. It uses a list comprehension to iterate through each string in the input list and checks if the substring is present in each string, including the substring as part of the new list if it is.  This solution is efficient and can be enhanced further by adding additional tests to ensure correctness.