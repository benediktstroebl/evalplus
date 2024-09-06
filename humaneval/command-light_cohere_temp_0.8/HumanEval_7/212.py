Here's a self-contained Python script with a function `filter_by_substring` that filters an input list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The above function takes two arguments: a list of strings (`strings`) and a substring (`substring`). It uses the `contains.contains()` method to check if each string in the list contains the given substring. 

The function returns a new list containing only the strings from the input list that contain the specified substring.