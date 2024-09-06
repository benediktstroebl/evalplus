```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that filters a list of strings to only contain the provided `substring`. It uses the `contains` built-in method to iterate over the list and check if each element contains the `substring` using the `contains` method. The resulting filtered list is then returned.