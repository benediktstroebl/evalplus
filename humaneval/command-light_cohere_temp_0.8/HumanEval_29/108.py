Here's the self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix parameter, and returns a new list containing only the strings from the input list that start with the given prefix. It uses the fact style of list comprehension to filter the strings by their prefix. 

This function is self-contained and can be used to solve the problem of filtering strings based on their prefix in a markdown code block.