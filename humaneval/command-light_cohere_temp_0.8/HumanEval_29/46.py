```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
Here's a Python script with a self-contained function that filters an input list of strings based on their prefix. The function uses the filtering technique where it examines each string in the input list to determine whether its prefix matches the given prefix. 

The script also includes unit tests to ensure the correctness of the filter_by_prefix function with various inputs.