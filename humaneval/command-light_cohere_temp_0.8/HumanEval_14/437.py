```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:2]] + [sub[0] for sub in string.find('abc', 1)]
```
Do you need help with anything else with Python programming?