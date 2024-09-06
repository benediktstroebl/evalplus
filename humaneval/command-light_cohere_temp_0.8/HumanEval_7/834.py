```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This Python function uses the contains() method to filter a list of strings and return a new list containing only the strings that contain the given substring. 
It takes two arguments: strings, which is the input list of strings, and substring, which is the substring to search for in the strings. The function returns a list of strings that contain the substring.