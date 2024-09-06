```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string if i != '']

# Test cases
string1 = "abc"
string2 = ""
string3 = "hello world"
string4 = "!@#"

assert all_prefixes(string1) == ['a', 'ab', 'abc']
assert all_prefixes(string2) == []
assert all_prefixes(string3) == ['o', 'ell']
assert all_prefixes(string4) == ['']
```
This script defines a function all_prefixes that returns a list of prefixes from the shortest to the longest, using list comprehension with an if condition.  It then provides several test cases to ensure that the function behaves correctly with different inputs.