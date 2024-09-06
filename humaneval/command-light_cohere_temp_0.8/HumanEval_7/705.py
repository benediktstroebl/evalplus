Here is a Python script that defines a function `filter_by_substring` that filters an input list of strings based on whether the strings contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The `contains` construct is used to iterate over the input list and check if each string contains the given substring. 
The output of this function is a new list containing only the strings from the original list that contain the specified substring.