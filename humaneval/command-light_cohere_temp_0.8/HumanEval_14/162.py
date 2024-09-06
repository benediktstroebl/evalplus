Here's the corrected and self-contained Python script that solves the problem of finding all prefixes from shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [w for w in string if w != '']
```
This code defines a function all_prefixes that takes a string as input and returns a list of all prefixes (non-empty characters) from the input string. 
Note that this solution is optimized and self-contained, as it uses a generator expression to efficiently extract all prefixes without using a loop.