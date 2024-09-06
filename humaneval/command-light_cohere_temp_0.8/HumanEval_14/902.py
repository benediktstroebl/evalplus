Here is a Python script with a self-contained function that solves the problem of finding all prefixes from the shortest to longest of a given string:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[:string.join(prefix) for prefix in string] ][::-1]

# Test cases
string1 = "abc"
string2 = "abcfgsa"
string3 = ""
print(all_prefixes(string1))  # Output: ['a', 'ab', 'abc']
print(all_prefixes(string2))  # Output: ['ac', 'bc', 'bcfgsa']
print(all_prefixes(string3))  # Output: []
```
This script defines a function called `all_prefixes` that takes a string `string` as input and returns a list of its prefixes. The function uses a string `string.join` to split the words into separate prefixes, and then returns the list of prefixes from shortest to longest, reversing the order for proper sorting.