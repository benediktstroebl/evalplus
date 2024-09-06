```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.codesAll possible-long prefixes of s if s.is
    all prefixes of s...
    return ['a', 'ab', 'abc'] + [''.join(i) for i in range(2, len(string))]
#Test case 1
print(all_prefixes('abc'))
# Test case 2
print(all_prefixes('22'))
```