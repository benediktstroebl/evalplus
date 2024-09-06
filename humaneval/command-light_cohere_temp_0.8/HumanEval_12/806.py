```python
from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    return max(strings, key=len)
# Tests
strings = ['a', 'bb', 'ccc']
print(longest(strings))  # Output: 'ccc'
strings = ['a', 'bb']
print(longest(strings))  # Output: 'bb'
strings = []
print(longest(strings))  # Output: None
strings = ['a', 'bb', 'ccc']
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'
```