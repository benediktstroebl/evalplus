Here is a Python script that contains a self-contained function that filters an input list of strings for a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
```

This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The function uses a process of iterating through each string in the input list, checking if the substring is present.

This function is self-contained as it does not depend on any other functions or modules.  It can be used to solve the given problem.