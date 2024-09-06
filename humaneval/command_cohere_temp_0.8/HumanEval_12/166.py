Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(set(strings).count(longest_string)) == 1 else longest_string[0]
```

This script defines a function called `longest` that takes a list of strings as input and returns either the longest string in the list, the first string among multiple longest strings, or None if the list is empty. It utilizes the `typing` module to include type annotations and uses the `max` function with a custom key argument based on string length to identify the longest string and the `set` function to identify distinct longest strings.