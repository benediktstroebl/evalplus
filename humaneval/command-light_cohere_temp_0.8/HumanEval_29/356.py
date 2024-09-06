```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]
```
The above Python script defines a function `filter_by_prefix` that takes in two parameters: a list of strings and a prefix string. The function uses the filter the using the list comprehension to filter the list of strings and return only those that start with the given prefix.