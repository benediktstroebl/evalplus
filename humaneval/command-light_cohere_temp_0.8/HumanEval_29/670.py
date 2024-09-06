Here is a self-contained Python script that includes a function called **`filter_by_prefix`** that filters an input list of strings based on a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function tests whether each string in the input list starts with the given prefix. It uses the Python's **`startswith`** method to accomplish this.