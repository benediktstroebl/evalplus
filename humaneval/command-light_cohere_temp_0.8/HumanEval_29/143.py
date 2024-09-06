Here's the self-contained Python script with the function `filter_by_prefix` that filters an input list of strings based on their prefix:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. 

It uses the `startswith` method of string in Python to check if each element in the strings list starts with the given prefix. 

Please note that this function is self-contained and can be used to filter lists of strings in various scenarios.