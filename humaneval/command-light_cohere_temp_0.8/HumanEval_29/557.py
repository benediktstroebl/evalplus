```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the filter technique to iterate over each string in the list and check if the prefix of the string is equal to the given prefix.