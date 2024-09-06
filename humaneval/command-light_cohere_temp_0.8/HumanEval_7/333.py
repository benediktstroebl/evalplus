```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
This Python function takes a list of strings and a substring as input and returns a new list of strings that contain the substring. It uses the search() function to find all occurrences of the substring in the input strings, and then returns a new list that contains only those strings. 

This is a self-contained function, as it does not require any external functions or classes to be called and can be run directly from the Python interpreter.