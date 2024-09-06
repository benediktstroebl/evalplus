```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function called **filter_by_prefix** that takes two parameters: a list of strings **strings** and a prefix **prefix**. The function uses a list comprehension to create a new list that contains only the strings from the input list that start with the given prefix. 

This function is useful when you want to filter out strings from a collection that share a specific prefix.