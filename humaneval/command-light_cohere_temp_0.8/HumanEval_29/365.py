Here is a self-contained Python script that includes a function called **`filter_by_prefix`** which solves the problem and passes all the corresponding tests: 
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **`filter_by_prefix`** that takes in a list of strings and a prefix, and returns a new list that contains only the strings from the original list that start with the given prefix. The test cases can also be run to verify the functionality of the function.