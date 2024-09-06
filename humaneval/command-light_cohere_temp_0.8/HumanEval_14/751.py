```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']
test_string = 'abc'
test_result = all_prefixes(test_string)
print(test_result)
```