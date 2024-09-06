```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char for char in string if char.isalpha()) for i, 0, in range(len(string))]

# Test cases
string1 = "abc"
string2 = "01234yab"
string3 = ""
print("Test case 1:", all_prefixes(string1))
# Expected Output: ['a', 'ab', 'abc']
print("Test case 2:", all_prefixes(string2))
# Expected Output: ['yab']
print("Test case 3:", all_prefixes(string3))
# Expected Output: []
```