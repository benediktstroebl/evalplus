```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function uses a list comprehension to filter the strings in the input list. The function is tested and can be used as a regular function in a Python script.