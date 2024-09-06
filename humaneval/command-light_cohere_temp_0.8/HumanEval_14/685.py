```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' if c.isalpha() else 'ab' if c.isupper() else 'a' else c for c in string]

#Test cases
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
print(all_prefixes('abcd'))  # Output: ['ab', 'abcd']
print(all_prefixes('xyz'))  # Should print an empty list
```