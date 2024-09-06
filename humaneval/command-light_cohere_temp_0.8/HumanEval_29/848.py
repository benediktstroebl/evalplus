```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This code implements a function called `filter_by_prefix` that takes in a list of strings and a prefix as input, and returns a new list that contains only the elements of the input list that start with the given prefix.