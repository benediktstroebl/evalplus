```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The function `filter_by_substring` filters an input list of strings and returns only the ones that contain the given substring. 
It takes two parameters:
- `strings`: A list of strings to filter.
- `substring`: The substring to search for in the strings

The function uses a list comprehension to iterate over each string in the input list. It uses the string.pw that the use the of a condition that checks if a string contains the given substring. 

This function is self-contained, and it can be used to filter a list of strings for ones that contain a given substring.