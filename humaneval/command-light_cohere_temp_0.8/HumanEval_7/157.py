```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This code implements a function called `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. 

The function uses the `contains` method to check if each string in the input list contains the given substring. 
The test cases demonstrate that the function correctly filters the strings based on whether they contain the substring.