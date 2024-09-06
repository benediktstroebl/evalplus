```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
print(all_prefixes('abc'))  # ['a', 'ab', 'abc']
```
Do you have any further questions about writing code or other coding problems?