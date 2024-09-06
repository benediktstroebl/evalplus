```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [x for x in string if x != '' and x not in {' ', '#', '@', '!', ','}]
```