```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.find(substring)]
```
The above Python function takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the substring. 

The function uses the `find()` method to check if each string contains the given substring. 

This function is self-contained, and it does not require any external functions or classes.