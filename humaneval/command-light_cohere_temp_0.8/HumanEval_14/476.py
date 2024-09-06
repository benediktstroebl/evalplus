Here's a solution to the given problem:

```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ' ')
```

This code defines a function all_prefixes that returns a list of prefixes from the shortest to longest, considering only non-space characters.  The list comprehension and the string characters that are not spaces are transformed into strings.