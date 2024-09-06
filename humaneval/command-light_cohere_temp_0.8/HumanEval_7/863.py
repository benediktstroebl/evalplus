Here is a self-contained Python script that defines a function filter_by_substring that filters a list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```
This script uses the List and str types from the typing module and defines a function filter_by_substring that takes a list of strings and a substring as input parameters. The function returns a filter the list of strings from the input list that contain the given substring.