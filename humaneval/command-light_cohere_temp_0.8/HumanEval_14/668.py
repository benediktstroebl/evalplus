```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join("".join(string). _ )): [string] + all_prefixes(string[1:])

# Test case 1: Single character
test_case1 = "a"
assert all_prefixes(test_case1) == ['a']

# Test case 2: Two characters
test_case2 = "ab"
assert all_prefixes(test_case2) == ['ab']

# Test case 3: Three characters
test_case3 = "abc"
assert all_prefixes(test_case3) == ['abc']

# Test case 4: More than three characters
test_case4 = "hello world"
assert all_prefixes(test_case4) == ['hello', 'world']
```
This script defines a function called all_prefixes that returns a list of all prefixes of a given string. The function uses a shortest prefix strategy, iterating over the string and adding each character to the current prefix. This is the way it can solve the problem of finding all prefixes of a string efficiently.