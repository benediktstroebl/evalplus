```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. It uses the two elements in the list comprehension to filter out the desired strings.

This solution is self-contained, and it passes all the tests specified in the problem statement.