```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code defines a function called **filter_by_substring** that filters a list of strings based on whether each element contains a given substring. The function uses the process that iterates through the input list of strings and uses the **find** method to check if each string contains the specified substring.