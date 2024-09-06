Here is a self-contained Python script that solves the problem of filtering strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The code uses the **startswith** method to check if each string in the input list starts with the given prefix. 

This script is self-contained and does not require any external modules or functions.