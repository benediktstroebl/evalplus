Here is a self-contained Python script with a function that filters an input list of strings based on a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function iterates through each string in the input list and checks if the string contains the given substring. The function returns a filtered list of strings that contain the specified substring.

This solution is self-contained as it does not require any external variables or functions to pass the test.