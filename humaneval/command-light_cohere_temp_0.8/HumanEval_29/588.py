```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This code implements a function `filter_by_prefix` that takes a list of strings and a prefix, then returns a new list with all elements that start with the given prefix. The code uses the using a generator expression to create the new list. The function is tested as it passes all the test cases and does not depend on the order of the input strings.