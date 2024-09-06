```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function that takes in a list of strings and a prefix, and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the Python list comprehension to filter the strings based on the given prefix. The function passes all tests since it returns the expected output for the given input.