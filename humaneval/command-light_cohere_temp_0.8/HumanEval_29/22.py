```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as parameters. It then creates a list comprehension, filtering only the strings that start with the specified prefix. 

This is a self-contained solution and passes all the tests.