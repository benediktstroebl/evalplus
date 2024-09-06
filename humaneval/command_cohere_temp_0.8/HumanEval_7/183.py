```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings that contain the given substring from the given list of strings.

Ensure the correctness of the typing module inclusion and the function signature, which are essential for type checking and code readability, respectively. Also, list comprehension is used elegantly to filter out the strings and return the desired result. 

This solution is efficient and follows Python best practices. Let me know if it works well for you, and if not, we can address any particular requirements you have!