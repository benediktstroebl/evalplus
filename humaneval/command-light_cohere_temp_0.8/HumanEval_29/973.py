Here's a self-contained Python script that implements the function filter_by_prefix from the previous prompt:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This script defines a function **filter_by_prefix** that takes in a list of strings and a prefix, and returns a new list that contains only the strings that start with the given prefix. The code uses the efficient list comprehension to filter the strings based on their prefix.