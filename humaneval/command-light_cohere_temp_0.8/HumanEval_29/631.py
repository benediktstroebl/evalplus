```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code provides a filter_by_prefix function that takes in a list of strings and a prefix.

This function returns a new list that contains only the elements from the input list that start with the given prefix.

The code uses the **startswith()** method to create a new list.