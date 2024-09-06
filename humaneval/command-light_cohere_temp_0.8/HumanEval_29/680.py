Here's the self-contained Python script with the function `filter_by_prefix` that filters an input list of strings based on their prefix:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filtered list of strings that start with the given prefix. The test case is also provided to pass the function test.