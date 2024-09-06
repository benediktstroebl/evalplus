```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python code defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input and returns a new list of strings that start with the specified prefix. It uses the full list comprehension to filter out the elements of the input list that match the given condition.