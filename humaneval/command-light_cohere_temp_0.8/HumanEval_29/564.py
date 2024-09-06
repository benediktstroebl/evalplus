Here is a Python script that contains a self-contained function that solves the problem you described:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    :e code handles List[str], the return list of strings that start with the given prefix.

    return:
    strings filtered by starting with the prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that takes in a list of strings and a prefix, and returns a new list of strings that start with that prefix. It uses the filter method to filter the list of strings based on their starting prefix. 

This function is self-contained, as it does not require any additional imported libraries or functions.