```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function named `filter_by_prefix`, which takes a list of strings and a prefix as input. The function returns a filter the list of all strings from the input list that start with the given prefix. 

This solution is efficient and uses a list comprehension to achieve the desired outcome.