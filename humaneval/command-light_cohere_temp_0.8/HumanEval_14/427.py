```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(prefix) for prefix in string.strings.split()]
shortest longest prefix in the string and returns the list of prefixes from shortest to longest.
# Test case 1
input: abc
print(all_prefixes('abc'))
# Expected Output ['a', 'ab', 'abc']
# Test case 2
input: "abc"
print(all_prefixes('abc'))
# Expected Output ['abc']
# Test case 3
input: "a"
print(all_prefixes('a'))
# Expected Output ['a']
# Test case 4
input: 
# empty string
print(all_prefixes(''))
# Expected Output []
```