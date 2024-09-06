```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function uses the contains() method to check if each string in the input list contains the given substring. 
It then returns a list of all strings from the input list that do contain the substring.