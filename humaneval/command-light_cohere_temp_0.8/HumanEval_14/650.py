Here's the code that implements the problem you mentioned:
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != '']
```
This function generates a list of all prefixes from the shortest to the longest, non-space characters in the input string.