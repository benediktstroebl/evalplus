```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This code implements a function called **filter_by_substring** that filters a list of strings for a given substring. It uses the basic Python list comprehension to achieve this.