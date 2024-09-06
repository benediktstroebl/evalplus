```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This script defines a function **filter_by_substring** that takes a list of strings and a substring as arguments, and it returns a new list containing only the strings from the input list that contain the given substring. 
The function uses the typing module to explicitly define the function's parameters and return type, ensuring better type safety and code clarity.