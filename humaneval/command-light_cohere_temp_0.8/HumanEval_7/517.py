```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The code you provided is a Python script that defines a function **filter_by_substring** that filters a list of strings for a given substring. 

The function uses the **contains** method to check if each string in the list contains the given substring. 
This function is self-contained and can be used to solve the problem of filtering strings that contain a given substring.