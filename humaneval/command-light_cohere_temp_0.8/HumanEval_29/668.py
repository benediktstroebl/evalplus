```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The above Python script defines a function **`filter_by_prefix`** that filters an input list of strings based on a given prefix. It uses the Python's list comprehension to filter out the elements that start with the specified prefix. The function works with any list of strings and returns a new list containing only the strings that match the given prefix. 

This function is a self-contained way to solve the problem and it passes all the tests with the given inputs.