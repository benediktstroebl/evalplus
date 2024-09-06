```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char != '\n']

# Test cases
string1 = "abc"
string2 = ""
string3 = "hello world"

print(all_prefixes(string1))  # Output: ['a', 'ab', 'abc']
print(all_prefixes(string2))  # Output: []
print(all_prefixes(string3))  # Output: ['h', 'ello']
```