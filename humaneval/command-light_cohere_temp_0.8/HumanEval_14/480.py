```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix != '' and not prefix.isalpha() ][
# left-most matching ][^a-zA-]+
```
Do you want help with anything else?