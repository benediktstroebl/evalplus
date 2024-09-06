Here's the self-contained Python script with a function that filters an input list of strings based on a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring) != - None]
```
This script defines a function that filters an input list of strings to retain only those that contain a given substring. The function utilizes the important List[str] and str types to ensure the input is correctly interpreted as strings.

The function returns a new list containing only the strings from the input list that contain the specified substring. 

This is a clear, well-contained way to solve a problem using Python and its typing features.