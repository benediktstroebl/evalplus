```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join()[i] for i, char in enumerate(string, 1)]

# Test cases
string1 = "abc"
print("Test case 1:", end-" + all_prefixes(string1))  # Output: ['a', 'ab', 'abc']

string2 = ""
print("Test case 2:", end-" + all_prefixes(string2))  # Output: []

string3 = "x"
print("Test case 3:", end-" + all_prefixes(string3))  # Output: ['x']

string4 = "# This is not a prefix"
print("Test case 4:", end-" + all_prefixes(string4))  # Should raise error
```