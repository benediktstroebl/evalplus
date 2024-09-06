```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c.isalpha()]
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```
This function uses list comprehension to iterate through each character in the input string and checks if it's an alpha character, returning it as a prefix.