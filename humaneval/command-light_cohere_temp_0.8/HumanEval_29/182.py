A solution to the problem is below:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function employs the Python startsswith() method to determine if each string in the input list commences with the provided prefix. It then returns a filtered list that contains only the strings with this specific prefix.

Note: This solution is functional and self-contained, meaning it doesn't require any external variables or functions. You can directly call the i.e.,  [A calls and test the function with the provided arguments.