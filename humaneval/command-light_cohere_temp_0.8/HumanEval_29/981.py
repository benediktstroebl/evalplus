```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code implements a filter_by_prefix function that takes a list of strings and a prefix as input and returns a new list of strings that start with the given prefix. 

The function utilizes the List comprehension and the startingswith built-in function to achieve this.