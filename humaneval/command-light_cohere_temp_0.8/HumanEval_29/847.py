```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the specified prefix. The test cases are provided to ensure the function's correctness.