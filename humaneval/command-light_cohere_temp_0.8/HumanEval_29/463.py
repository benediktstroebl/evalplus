Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This script defines a function called **filter_by_prefix** that takes in a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the specified prefix.