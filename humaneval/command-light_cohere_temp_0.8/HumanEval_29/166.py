Certainly! Here's a Python script with a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. It uses the value of the list comprehension to filter the strings based on their prefixes.