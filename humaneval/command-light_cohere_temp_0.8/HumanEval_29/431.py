Certainly! Here is a Python script with a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix."""
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the specific type hint `List[str]` and `List[Class[T]]` to ensure that the input list is passed correctly as a variable of type `List[str]` and that the function will return the correct result.