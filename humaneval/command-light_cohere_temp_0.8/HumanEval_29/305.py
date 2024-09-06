Here is a self-contained Python script that defines a function `filter_by_prefix`, which takes a list of strings and a prefix as arguments, and returns a new list containing only the strings from the input list that start with the specified prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [s for s in strings if s.startswith(prefix)]
```

This function uses a list comprehension to iterate over each string in the input list. It checks if the the start of each string is equal to the provided prefix. The function returns a list containing only the strings that satisfy this condition.