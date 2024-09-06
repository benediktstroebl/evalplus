```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python code implements a function called **filter_by_substring** that filters an input list of strings and returns a new list containing only those strings that contain a given substring. 

The function utilizes the list comprehension with the **find** method to locate all occurrences of the substring within the strings.