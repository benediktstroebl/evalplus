Here's the solution:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a `filter_by_substring` function that filters a list of strings based on whether the substring is present in each string. The function utilizes the `contains` to iterate over the list of strings and checks if each string contains the given substring using the `contains` method. The function returns a list of all strings that contain the specified substring, as the result.