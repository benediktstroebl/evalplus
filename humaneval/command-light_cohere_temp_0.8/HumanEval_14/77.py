```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string if c.isalpha()]

# Test the function with some input strings
assertEqual(all_prefixes('abc'), ['a', 'ab', 'abc'])
assertEqual(all_prefixes('abcde'), ['abcd', 'abcde'])
assertEqual(all_prefixes('aa'), [])
assertEqual(all_prefixes(''), []
```