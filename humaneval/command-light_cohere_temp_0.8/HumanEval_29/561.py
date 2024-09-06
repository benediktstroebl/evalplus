Certainly! Here's a self-contained Python script that includes the function `filter_by_prefix` and passes the test cases: 
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function uses the `startswith` method to check if each string in the list starts with the given `prefix`. The function returns a new list containing only the strings that match this condition. 

This is just one way this function could be implemented, and you can always find the appropriate way that works best for your problem.