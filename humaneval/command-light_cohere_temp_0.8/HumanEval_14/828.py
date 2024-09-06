```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char for char in string if char.isalpha() or 123456])  # check for uppercase characters

# Test cases 
print(all_prefixes('abc'))
print(all_prefixes('ABC'))
print(all_prefixes('123ABC'))
print(all_prefixes('A123bc'))
```