Below is a Python script that contains a self-contained function called `filter_by_substring` that filters an input list of strings based on whether the strings contain a given substring:

```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The `contains` method checks if a given string contains the given substring using the `contains` method of the string object. The `List` method of the list is then used to filter the list and return a new list containing only the strings that contain the substring.