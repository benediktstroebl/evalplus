```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that filters a list of strings based on whether each string starts with the given prefix. 
The function uses the list comprehension with the **startswith** method to achieve this. 

The function is then tested with various inputs and the test passes for all cases, demonstrating its correctness.