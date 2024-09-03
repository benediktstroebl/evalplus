Here is a self-contained Python script that defines a function `filter_by_prefix` that filters an input list of strings based on their prefix:
```python
from typing import List
import re

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if re.find(prefix, string)]
```

This function utilizes the `re.find()` method from part of the `re` module, which is designed to search for a match within a string. The function returns a list of strings from the input list that have the given `prefix` as their starting characters.