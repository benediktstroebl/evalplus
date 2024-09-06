```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function returns a list of strings from the input list `strings` that have the given `prefix`. It uses the `startswith` method which is both Pythonic and more readable than the `startswith` method from `string` module.