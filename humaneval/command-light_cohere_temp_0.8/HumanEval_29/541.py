Certainly, here is a Python script that includes a self-contained function `filter_by_prefix` which correctly filters strings by their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This function uses the Python Informer operation to filter the strings and then returns a new list with the filtered strings.