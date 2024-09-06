```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [str for str in string if str.isalpha()}

all_prefixes('abc')
```