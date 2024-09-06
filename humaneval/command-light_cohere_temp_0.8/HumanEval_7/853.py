Here's the self-contained Python script with a function that filters an input list of strings for a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that filters an input list of strings to include only those that contain a given substring. The function uses the string slicing and the contains() method to achieve this. This function is a way, is self-contained and does not require any external or external functions to function.