```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring)]
```
The provided Python script defines a function called **filter_by_substring** that takes a list of strings and a substring as input. The function uses the search in each string using the find() method and returns a new list that contains only the strings that contain the given substring. 

This function is self-contained, and it efficiently filters the input strings based on the given substring.