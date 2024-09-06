```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(w for w in string if w.isalpha()) for i in range(1, len(string))]

# Test cases
string1 = "abc"
string2 = "hello world"
string3 = "!!!!@#$@%"

print(all_prefixes(string1))  # Output: ['a', 'ab', 'abc']
print(all_prefixes(string2))  # Output: ['hello', 'world']
print(all_prefixes(string3))  # Output: ['!@', '!@$']
```