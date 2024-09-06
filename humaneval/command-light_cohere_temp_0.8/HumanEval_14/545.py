```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c != '']
```
This function iterates through each character in the input string and adds non-space characters to a new string, creating a list of prefixes from shortest to longest.

Please note that this solution is fully self-contained within the Python script and does not require any external modules or functions.