```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string.
    # Additional test of or strings in the string
    # Bounds can be improved and even if it's better, just for clarity and concisistency, a better way is to use slice notation:
    return [i for i in string if i != '']
```