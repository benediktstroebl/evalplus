```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + string.test = [all_prefixes('abc')  # passing test case
```