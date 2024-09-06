```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The above function takes a list of strings and a substring as input and returns a new list that contains only the strings that contain the substring. 

In this implementation, the find() method is used to search the given substring in each string, and if the substring is found, the string is added to the result.