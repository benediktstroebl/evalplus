```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with that prefix. It uses the ** list comprehension to filter the input list based on the given prefix. 

This function is a complete implementation, and it passes all the test cases.