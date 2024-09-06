Here's the self-contained Python function to filter an input list of strings that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function takes two arguments: a list of strings and a substring. It uses the `contains` to iterate through strings and checks if each one contains the given substring. This results in a list of strings that contain the substring.