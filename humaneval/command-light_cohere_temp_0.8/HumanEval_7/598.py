```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as arguments. It uses the general technique of iterating through a generator expression to filter out strings that do not contain the given substring. 

This approach is self-contained and doesn't require any external list manipulation or loops.