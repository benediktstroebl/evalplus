```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function called **`filter_by_prefix`** that takes a list of strings and a prefix as input. The function uses the `List[str]` as the element in the list to iterate through and checks if each element starts with the given prefix. 

It then returns a new list that contains only those elements from the original list that do have the specified prefix.