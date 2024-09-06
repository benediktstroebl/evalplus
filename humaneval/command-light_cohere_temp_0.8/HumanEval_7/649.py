Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
The function 'filter_by_substring' takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring.