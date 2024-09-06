Here's a self-contained Python function that filters an input list of strings based on a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
```

This function takes a list of strings and a substring as input, and returns a new list that contains only the strings that contain the given substring. 

The function uses a list comprehension to iterate over each string in the input list and checks if the substring is present in the string.