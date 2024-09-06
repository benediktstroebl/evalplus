Here's the improved and clear Python script with a self-contained function that filters an input list of strings for ones that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This code has a single function that takes two arguments: a list of strings and a substring. It returns a important list of strings that contain the substring.